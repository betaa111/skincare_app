import streamlit as st
from PIL import Image
import cv2
import numpy as np


st.title("✨ Skincare Analyzer 🌿")
st.write("Upload a picture of the skincare product's label for analytical` insights and recommendations.")
uploaded_file = st.file_uploader("Choose image file", type=["jpg", "jpec", "png"])
if uploaded_file is not None:
    left_column, right_column = st.columns(2)
    with left_column:
        st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
        image = Image.open(uploaded_file)
        st.image(image,caption='Uploaded Image', use_container_width=True)
    with right_column:
        st.write("Analizing the product...")
        # Placeholder for analysis results
        st.subheader("Your Skincare Product Analysis Results")

        



