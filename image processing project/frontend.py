import streamlit as st
import cv2
import numpy as np
from PIL import Image
from backend import *

# --------------implement Screen-------------
# --------First upload image-----------------
# -----------Convert image to array----------
# ---------Second Choose Filter from box-----


def main():
    st.header("Welcome to our project for DIP")
    image_uploader = st.file_uploader('please upload an image file ....', type=['jpg', 'png', 'jpeg'])
    if image_uploader is not None:
        image = Image.open(image_uploader)
        image_cv2 = np.array(image)

        # ----------- start convert BGR to RGB -----------
        image_cv2 = cv2.cvtColor(image_cv2, cv2.COLOR_BGR2BGRA)
        option = st.selectbox('Select your filter', (
            'Select', 'Edge Detection', 'Grayscale', 'Negative Transformation', 'Gaussian Blur', 'Reduce Noise',
            'Sharping'))
        st.write('You selected:', option)
        # ----------- end convert BGR to RGB --------------

        # --------- start Choose from selectbox ------------
        if option == 'Select':
            pass
        # --------- end Choose from selectbox---------------

        # -------- start Edge Detection in selectionbox-----
        elif option == 'Edge Detection':
            st.header('Input image')
            st.image(image)
            st.markdown('Image after Edge Detection')
            st.image(edge_detection(image_cv2))
        # -------- end Edge Detection in selectionbox-----

        # -------- start Gray Scale in selectionbox-------
        elif option == 'Grayscale':
            st.header('Input image')
            st.image(image)
            st.markdown('Image after Grayscale')
            st.image(gray_scale(image_cv2))
        # -------- end Gray Scale in selectionbox-------

        # ------ start Negative Transformationin selectionbox ---------
        elif option == 'Negative Transformation':
            st.header('Input image')
            st.image(image)
            st.markdown('Image after Negative Transformation')
            st.image(negative_transformation(image_cv2))
        # ------ end Negative Transformationin selectionbox---------

        # ------ start Gaussian Blur in selectionbox ----------------
        elif option == 'Gaussian Blur':
            st.header('Input image')
            st.image(image)
            st.markdown('Image after Gaussian Blurring')
            st.image(gaussian_blur(image_cv2))
        # ------ end Gaussian Blur in selectionbox ----------------

        # -------- start Reduce Noise in selectionbox -------------
        elif option == 'Reduce Noise':
            st.header('Input image')
            st.image(image)
            st.markdown('Image after Remove Noise')
            st.image(reduce_noise(image_cv2))
        # -------- end Reduce Noise in selectionbox -------------

        # ----------- start Sharping in selectionbox--------------
        elif option == 'Sharping':
            st.header('Input image')
            st.image(image)
            st.markdown('Image after Sharping')
            st.image(sharp_image(image_cv2))
        # ----------- end Sharping in selectionbox--------------

        else:
            pass


if __name__ == "__main__":
    main()
