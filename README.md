# AI Image Description Generator 🤖

This is a Streamlit-based web application that generates AI-powered image descriptions using Salesforce's BLIP image captioning model. Users can upload images, generate descriptions, and download results in CSV format.

## Features
- Upload multiple images via the sidebar
- Preview uploaded images in a table format
- Generate AI-powered descriptions for images
- Download descriptions as a CSV file

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/ai-image-description.git
   cd ai-image-description
   ```

2. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Dependencies

- `streamlit`
- `transformers`
- `torch`
- `Pillow`
- `pandas`
- `base64`

Install them manually if needed:
```sh
pip install streamlit transformers torch Pillow pandas
```

## Usage

Run the Streamlit app using:
```sh
streamlit run app.py
```

## Approach & Model Information

This project utilizes Salesforce's BLIP (Bootstrapping Language-Image Pre-training) model for image captioning. BLIP is a transformer-based vision-language model that generates textual descriptions of images. The application processes uploaded images and passes them through the BLIP model to generate accurate and context-aware captions.

## Function Details

### `to_base64(uploaded_file)`
Converts an uploaded image file into a base64-encoded string for easy storage and display within the application.

### `generate_df()`
Creates a Pandas DataFrame to store image data, including base64-encoded images, filenames, and generated descriptions.

### `render_df()`
Displays the DataFrame in a user-friendly table format within Streamlit, allowing users to view image previews and generated descriptions.

### `generate_description(image_base64)`
Decodes the base64-encoded image, processes it using the BLIP model, and generates a textual description.

### `update_df()`
Iterates through the DataFrame and fills empty description fields by calling `generate_description()` for each uploaded image.

## How It Works

1. Upload images via the sidebar.
2. Click **"Generate Image Description"** to generate captions.
3. Download the results as a CSV file if needed.

![image](https://github.com/user-attachments/assets/a5841c15-ba91-49b7-9167-411ddbaadb6e)

## License

This project is licensed under the MIT License.
