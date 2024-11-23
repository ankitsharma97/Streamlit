import streamlit as st
from PIL import Image
import pytesseract
import numpy as np
import cv2

# Configure Tesseract OCR (Ensure Tesseract is installed on your system)
pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract"

# Title and description
st.title("🖼️ Image to Text Converter")
st.write(
    """
    This application extracts text from images using Optical Character Recognition (OCR).
    Upload an image to get started!
    """
)

# File uploader
uploaded_image = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])

if uploaded_image:
    # Display uploaded image
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Pre-processing options
    st.sidebar.header("Image Preprocessing Options")
    grayscale = st.sidebar.checkbox("Convert to Grayscale")
    thresholding = st.sidebar.checkbox("Apply Thresholding")

    # Convert to numpy array for OpenCV processing
    image_np = np.array(image)

    # Grayscale conversion
    if grayscale:
        image_np = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)
        st.image(image_np, caption="Grayscale Image", use_column_width=True, channels="GRAY")

    # Apply thresholding
    if thresholding:
        _, image_np = cv2.threshold(image_np, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        st.image(image_np, caption="Thresholded Image", use_column_width=True, channels="GRAY")

    # OCR Processing
    with st.spinner("Extracting text from the image..."):
        extracted_text = pytesseract.image_to_string(image_np)

    # Display extracted text
    st.subheader("Extracted Text")
    if extracted_text.strip():
        st.text_area("Text", extracted_text, height=300)

        # Download button
        st.download_button(
            label="📥 Download Extracted Text",
            data=extracted_text,
            file_name="extracted_text.txt",
            mime="text/plain",
        )
    else:
        st.warning("No text found in the image. Try a different image or adjust preprocessing options.")

else:
    st.info("Please upload an image to start.")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using [Streamlit](https://streamlit.io/) and Tesseract-OCR.")
