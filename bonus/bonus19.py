import streamlit as st
from PIL import Image

with st.expander('Start Camera'):

    # start the camera
    cam_image = st.camera_input('Camera')

# feature to upload an image
uploaded_image = st.file_uploader('Upload Image', 
                                  type=['jpg', 'jpeg', 'png'])
    
if cam_image:

        # Create a pillow image instance
        img = Image.open(cam_image)

        # Convert the pillow image to grayscale
        gray_img = img.convert('L')

        # Render the grayscale image on the webpage
        st.image(gray_img)

if uploaded_image:

        # Create a pillow image instance
        img = Image.open(uploaded_image)

        # Convert the pillow image to grayscale
        gray_img = img.convert('L')

        # Render the grayscale image on the webpage
        st.image(gray_img)