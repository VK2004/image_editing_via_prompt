import streamlit as st
import cv2
from nlp_model import chat
from PIL import Image
from io import BytesIO
import numpy as np
import re
import os

uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
if uploaded_file is not None:
    # Open the image file
    image_bytes = uploaded_file.read()
    image = Image.open(BytesIO(image_bytes))

    # Display the original image
    st.image(image, caption="Original Image")

tx = st.text_input("Prompt", )
results_list, num_from_prommpt = chat(tx)

st.write("Here are the things that you wanna do:", results_list)
st.write("Data values:", num_from_prommpt)
