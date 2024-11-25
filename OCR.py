import streamlit as st
import pytesseract
import cv2
import numpy as np
from PIL import Image
import re
import pytesseract
import os

os.environ['TESSDATA_PREFIX'] = r'C:\Program Files\Tesseract-OCR\tessdata'
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Title of the web app
st.title("OCR Text Extraction and Search")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read the image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Classifying...")

    # Convert image to array and apply OCR
    image_array = np.array(image)
    gray = cv2.cvtColor(image_array, cv2.COLOR_BGR2GRAY)

    # Use Tesseract to extract text
    extracted_text = pytesseract.image_to_string(gray, lang='eng+hin')

    # Display the extracted text
    st.subheader("Extracted Text:")
    st.write(extracted_text)

    # Keyword search functionality
    keyword = st.text_input("Enter a keyword to search:")
    if keyword:
        matches = re.findall(rf"({re.escape(keyword)})", extracted_text, re.IGNORECASE)
        if matches:
            st.success(f"Keyword '{keyword}' found {len(matches)} time(s)!")
            st.markdown(f"**Matching sections:** {extracted_text}")
        else:
            st.warning(f"Keyword '{keyword}' not found.")
