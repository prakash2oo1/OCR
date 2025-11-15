import streamlit as st
import cv2
import numpy as np
from PIL import Image
import re
import easyocr

# Initialize EasyOCR Reader
reader = easyocr.Reader(['en', 'hi'])

# Title of the web app
st.title("OCR Text Extraction and Search")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    try:
        # Read the image
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image.', use_column_width=True)
        st.write("")
        st.write("Processing the image...")

        # Convert image to array and apply OCR
        image_array = np.array(image)
        gray = cv2.cvtColor(image_array, cv2.COLOR_BGR2GRAY)

        # Use EasyOCR to extract text
        result = reader.readtext(gray)
        extracted_text = " ".join([text[1] for text in result])

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

    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")

else:
    st.info("Please upload an image to start the OCR process.")
