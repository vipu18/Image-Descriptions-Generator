import streamlit as st
import base64
import pandas as pd
import torch
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import io


# Main page
st.set_page_config(
    page_title="Image to Text",
    page_icon="📸",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Title
st.title("AI Image Description Generator 🤖")

# Sidebar - Upload images
with st.sidebar:
    st.title("Upload Your Image")
    uploaded_files = st.file_uploader(label=" ", accept_multiple_files=True)

# Convert image to base64
def to_base64(uploaded_file):
    file_buffer = uploaded_file.read()
    b64 = base64.b64encode(file_buffer).decode()
    return f"data:image/png;base64,{b64}"

# Store images in a dataframe
def generate_df():
    st.session_state.df = pd.DataFrame(
        {
            "image": [to_base64(img) for img in st.session_state.images],
            "name": [img.name for img in st.session_state.images],
            "description": [""] * len(st.session_state.images),
        }
    )

# Render the dataframe in a table
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

# Load BLIP model and processor
blip_processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
blip_model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Generate description
def generate_description(image_base64):
    # Convert base64 to image
    image_data = base64.b64decode(image_base64.split(",")[1])
    image = Image.open(io.BytesIO(image_data)).convert("RGB")

    # Process the image
    inputs = blip_processor(images=image, return_tensors="pt")

    # Generate caption
    output = blip_model.generate(**inputs)
    caption = blip_processor.decode(output[0], skip_special_tokens=True)

    return caption

# Add description to dataframe
def update_df():
    if "df" in st.session_state:
        for index, row in st.session_state.df.iterrows():
            if not row["description"]:  # Check if description is empty
                st.session_state.df.at[index, "description"] = generate_description(row["image"])

# Ensure images exist before processing
if uploaded_files:
    st.session_state.images = uploaded_files
    generate_df()

    st.text_input("Prompt", value="What's in the image?", key="text_prompt")

    col1, col2 = st.columns([1, 1])

    with col1:
        if st.button("Generate Image Description", use_container_width=True):
            update_df()

    with col2:
        st.download_button(
            "Download as CSV",
            st.session_state.df.drop(["image"], axis=1).to_csv(index=False),
            "description.csv",
            "text/csv",
            use_container_width=True,
        )

    render_df()
