<p align="center"><h1 align="center">AI-IMAGE-DESCRIPTION-GENERATOR</h1></p>
<p align="center">
<em><code>❯ AI-Powered Image Captioning with Salesforce BLIP Model</code></em>
</p>
<p align="center">
<img src="https://img.shields.io/github/license/username/ai-image-description-generator?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
<img src="https://img.shields.io/github/last-commit/username/ai-image-description-generator?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
<img src="https://img.shields.io/github/languages/top/username/ai-image-description-generator?style=default&color=0080ff" alt="repo-top-language">
<img src="https://img.shields.io/github/languages/count/username/ai-image-description-generator?style=default&color=0080ff" alt="repo-language-count">
</p>
<p align="center"><!-- default option, no dependency badges. -->
</p>
<p align="center">
<!-- default option, no dependency badges. -->
</p>
<br>

##  Table of Contents

- [ Overview](#-overview)
- [ Features](#-features)
- [ Project Structure](#-project-structure)
  - [ Project Index](#-project-index)
- [ Getting Started](#-getting-started)
  - [ Prerequisites](#-prerequisites)
  - [ Installation](#-installation)
  - [ Usage](#-usage)
  - [ Testing](#-testing)
- [ Project Roadmap](#-project-roadmap)
- [ Contributing](#-contributing)
- [ License](#-license)
- [ Acknowledgments](#-acknowledgments)

---

##  Overview

The AI Image Description Generator is a sophisticated Streamlit-powered web application that leverages Salesforce's BLIP (Bootstrapping Language-Image Pre-training) model to generate accurate and context-aware textual descriptions for uploaded images. This application provides a seamless interface for batch image processing with no dependency on paid APIs or external cloud services.

The system processes images locally using state-of-the-art transformer-based vision-language models, enabling users to upload multiple images simultaneously, generate AI-powered captions, preview results in an organized table format, and export descriptions as CSV files for further analysis or documentation purposes.

---

##  Features

<code>❯ **Core Image Processing**</code>
- **Multi-Image Upload**: Simultaneous upload and processing of multiple image files through an intuitive sidebar interface
- **AI-Powered Captioning**: Advanced image-to-text generation using Salesforce's BLIP transformer model
- **Real-time Preview**: Interactive table view with image thumbnails, filenames, and generated descriptions
- **Batch Processing**: Efficient processing of multiple images with automatic description generation

<code>❯ **User Interface Features**</code>
- **Streamlit Web Interface**: Clean, responsive web application with wide layout and expandable sidebar
- **Interactive Data Editor**: Customizable table with image preview columns, filename display, and description fields
- **Custom Prompting**: Configurable text prompts for description generation context
- **CSV Export**: One-click download of image names and descriptions in CSV format

<code>❯ **Technical Capabilities**</code>
- **Local Processing**: Complete offline functionality with no external API dependencies
- **Base64 Encoding**: Efficient image storage and display using base64 conversion
- **Session Management**: Persistent data storage during application usage
- **Memory Optimization**: Efficient handling of image data and model inference

---

##  Project Structure

```sh
└── ai-image-description-generator/
    ├── .gitattributes
    ├── Image-Descriptions-Generator.code-workspace
    ├── app.py
    ├── README.md
    └── requirements.txt
```

###  Project Index
<details open>
<summary><b><code>AI-IMAGE-DESCRIPTION-GENERATOR/</code></b></summary>
<details> <!-- __root__ Submodule -->
<summary><b>__root__</b></summary>
<blockquote>
<table>
<tr>
<td><b><a href='https://github.com/username/ai-image-description-generator/blob/master/app.py'>app.py</a></b></td>
<td><code>❯ Main Streamlit application with BLIP model integration, image processing pipeline, and interactive UI components</code></td>
</tr>
<tr>
<td><b><a href='https://github.com/username/ai-image-description-generator/blob/master/requirements.txt'>requirements.txt</a></b></td>
<td><code>❯ Python dependencies including Streamlit, PyTorch, Transformers, and image processing libraries</code></td>
</tr>
<tr>
<td><b><a href='https://github.com/username/ai-image-description-generator/blob/master/README.md'>README.md</a></b></td>
<td><code>❯ Comprehensive project documentation with installation guide, usage instructions, and technical details</code></td>
</tr>
<tr>
<td><b><a href='https://github.com/username/ai-image-description-generator/blob/master/.gitattributes'>.gitattributes</a></b></td>
<td><code>❯ Git configuration file defining line ending and file handling attributes for cross-platform compatibility</code></td>
</tr>
<tr>
<td><b><a href='https://github.com/username/ai-image-description-generator/blob/master/Image-Descriptions-Generator.code-workspace'>Image-Descriptions-Generator.code-workspace</a></b></td>
<td><code>❯ VS Code workspace configuration file for optimized development environment setup</code></td>
</tr>
</table>
</blockquote>
</details>
</details>

---
##  Getting Started

###  Prerequisites

Before getting started with ai-image-description-generator, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python 3.8+
- **Package Manager:** Pip
- **System Requirements:** CUDA-compatible GPU (optional, for faster inference)
- **Memory Requirements:** Minimum 4GB RAM (8GB recommended for optimal performance)

###  Installation

Install ai-image-description-generator using one of the following methods:

**Build from source:**

1. Clone the ai-image-description-generator repository:
```sh
❯ git clone https://github.com/username/ai-image-description-generator
```

2. Navigate to the project directory:
```sh
❯ cd ai-image-description-generator
```

3. Create a virtual environment (recommended):
```sh
❯ python -m venv venv
❯ source venv/bin/activate  # On Windows: venv\\Scripts\\activate
```

4. Install the project dependencies:

**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style=default&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pip install -r requirements.txt
```

**Note:** The first run will automatically download the BLIP model (~2GB) from Hugging Face Hub.

###  Usage

Run ai-image-description-generator using the following command:

**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style=default&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ streamlit run app.py
```

The application will launch in your default web browser at `http://localhost:8501`. Follow these steps:

1. **Upload Images**: Use the sidebar to upload one or multiple image files (JPG, PNG, GIF supported)
2. **Preview Images**: View uploaded images with their filenames in the main table interface
3. **Customize Prompt**: Modify the text prompt if needed (default: "What's in the image?")
4. **Generate Descriptions**: Click "Generate Image Description" to process all uploaded images
5. **Export Results**: Download the results as a CSV file containing filenames and descriptions

**Supported Image Formats:** JPEG, PNG, GIF, BMP, TIFF

###  Testing

Run manual tests using the following approach:

**Functional Testing:**
```sh
❯ # Test with sample images of different formats and sizes
❯ # Verify model loading and inference pipeline
❯ # Test CSV export functionality
```

**Performance Testing:**
- Test batch processing with 10+ images
- Monitor memory usage during model inference
- Verify handling of large image files (>10MB)

**UI Testing:**
- Test responsive design on different screen sizes
- Verify sidebar functionality and file upload
- Test data editor interactions and CSV download

---
##  Project Roadmap

- [X] **`Core Image Captioning`**: <strike>Implement BLIP model integration with Streamlit interface</strike>
- [X] **`Batch Processing`**: <strike>Add support for multiple image upload and processing</strike>
- [X] **`CSV Export`**: <strike>Enable download of results in structured format</strike>
- [ ] **`Model Options`**: Add support for alternative captioning models (CLIP, GPT-4V)
- [ ] **`Custom Training`**: Implement fine-tuning capabilities for domain-specific captions
- [ ] **`API Integration`**: Add REST API endpoints for programmatic access
- [ ] **`Cloud Deployment`**: Deploy to cloud platforms with scalable infrastructure
- [ ] **`Advanced Analytics`**: Add caption quality metrics and confidence scores
- [ ] **`Multi-language Support`**: Extend captioning to multiple languages

---

##  Contributing

- **💬 [Join the Discussions](https://github.com/username/ai-image-description-generator/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/username/ai-image-description-generator/issues)**: Submit bugs found or log feature requests for the `ai-image-description-generator` project.
- **💡 [Submit Pull Requests](https://github.com/username/ai-image-description-generator/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/username/ai-image-description-generator
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com/username/ai-image-description-generator/graphs/contributors">
      <img src="https://contrib.rocks/image?repo=username/ai-image-description-generator">
   </a>
</p>
</details>

---

##  License

This project is protected under the [MIT License](https://choosealicense.com/licenses/mit/) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/mit/) file.

---

##  Acknowledgments

- **Salesforce Research**: For developing and open-sourcing the BLIP (Bootstrapping Language-Image Pre-training) model
- **Hugging Face**: For providing the Transformers library and model hub infrastructure
- **Streamlit Team**: For creating an excellent framework for rapid ML application development
- **PyTorch Community**: For the robust deep learning framework powering the image processing pipeline
- **Open Source Contributors**: Thanks to all contributors who help improve computer vision and NLP technologies
