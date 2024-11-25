import pytesseract
import os
import cv2
import streamlit as st

# Set the Tesseract command path
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

# Set the TESSDATA_PREFIX environment variable
os.environ['TESSDATA_PREFIX'] = '/usr/share/tesseract-ocr/4.00/'

# Load the image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png"])
if uploaded_file:
    image_array = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), 1)
    gray = cv2.cvtColor(image_array, cv2.COLOR_BGR2GRAY)

    # Use Tesseract to extract text
    try:
        extracted_text = pytesseract.image_to_string(gray, lang='eng+hin')
        st.subheader("Extracted Text:")
        st.text(extracted_text)
    except Exception as e:
        st.error(f"Error extracting text: {e}")
