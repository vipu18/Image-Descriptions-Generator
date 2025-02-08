import streamlit as st
import base64
import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI Client
client = OpenAI()

#main page
st.set_page_config(
    page_title="Image to Text",
    page_icon = "📸",
    layout = "wide",
    initial_sidebar_state = "expanded"
)

#title
st.title(" AI Image Descriptiion Generator 🤖")

#sidebar
with st.sidebar:
    st.title("Upload Your Image")
    st.session_state.images = st.file_uploader(label= " ", accept_multiple_files=True)

#images to base64
def to_base64(uploaded_file):
    file_buffer = uploaded_file.read()
    b64 = base64.b64encode(file_buffer).decode()
    return f"data:image/png;base64,{b64}"

#store images in a dataframe
def generate_df():
    st.session_state.df = pd.DataFrame(
        {
        "image_id": [img.file_id for img in st.session_state.images],
        "image": [to_base64(img) for img in st.session_state.images],
        "name": [img.name for img in st.session_state.images],
        "description": [""] * len(st.session_state.images),
        }
    )

#render the dataframe in table 
def render_df():
    st.data_editor(
        st.session_state.df,
        column_config={
            "image": st.column_config.ImageColumn(
                "Preview Image", help="Image preview", width=100
            ),
            "name": st.column_config.Column("Name", help="Image name", width=200),
            "description": st.column_config.Column(
                "Description", help="Image description", width=800
            ),
        },
        hide_index=True,
        height=500,
        column_order=["image", "name", "description"],
        use_container_width=True,
    )

#generate description
def generate_description(image_base64):
    response = client.chat.completions.create(
        model = "gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {'type': "text", "text": st.session_state.text_prompt},
                    {
                        "type": "image_url",
                        "image_url":{
                            "url": image_base64,
                        },
                    },
                ],
            },
        ],
        max_tokens = 50,
    )
    return response.choices[0].message['content']

#add description
def update_df():
    st.session_state.df["description"] = st.session_state.df["image"].apply(generate_description)

if st.session_state.images:
    generate_df()

    st.text_input("Prompt", value ="what's in the image?", key ="text_prompt")

    col1, col2 = st.columns([1,1])

    with col1:
        if st.button("Generate Image Description", use_container_width=True):
            update_df()

    with col2:
        st.download_button(
            "Download as CSV",
            st.session_state.df.drop(['image', "image_id"], axis=1).to_csv(index=False),
            "decription.csv",
            "text/csv",
            use_container_width=True
        )

    render_df()