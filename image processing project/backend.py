import cv2
import numpy as np
from PIL import Image

# --------------- start image to display ---------------
def wrapAffine(image):
    rows, cols, ch = image.shape
    pts1 = np.float32([[50, 50],
                       [200, 50],
                       [50, 200]])

    pts2 = np.float32([[50, 100],
                       [200, 50],
                       [150, 200]])

    points = cv2.getAffineTransform(pts1, pts2)
    img = cv2.warpAffine(image, points, (cols, rows))
    img_conv = Image.fromarray(img)
    return img_conv
# --------------- end image to display ---------------

# --------------- start Edge Detection ---------------
def edge_detection(image):
    edges = cv2.Canny(image, 40, 80, L2gradient=True)
    img_conv = Image.fromarray(edges)
    return img_conv
# --------------- end Edge Detection -----------------

# --------------- start Gray Scale -----------------
def gray_scale(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img_conv = Image.fromarray(gray_image)
    return img_conv
# --------------- end Gray Scale --------------------

# --------------- start Negative Transformation --------------------
def negative_transformation(image):
    height, width, _ = image.shape
    for i in range(0, height - 1):
        for j in range(0, width - 1):
            pixel = image[i][j]
            pixel[0] = 255 - pixel[0]
            pixel[1] = 255 - pixel[1]
            pixel[2] = 255 - pixel[2]
    return image
# --------------- end Negative Transformation ----------------------

# --------------- start Gaussian Blur ---------------
def gaussian_blur(image):
    Blur = cv2.GaussianBlur(image, (5, 5), cv2.BORDER_DEFAULT)
    img_conv = Image.fromarray(Blur)
    return img_conv
# --------------- end Gaussian Blur -----------------

# ----------------- start Reduce noise -----------------
def reduce_noise(image):
    '''InputArray src,
    OutputArray dst,
    float h = 20,
    float hColor = 20,
    int templateWindowSize = 7,
    int searchWindowSize = 21'''
    # NON-LOCAL MEANS DENOISING ALGORITHM
    noiseless_image_colored = cv2.fastNlMeansDenoisingColored(image, None, 20, 20, 7, 21)
    img_conv = Image.fromarray(noiseless_image_colored)
    return img_conv
# ----------------- end Reduce noise -----------------

# ----------------- start Sharpening -----------------
def sharp_image(image):
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])
    image_sharp = cv2.filter2D(src=image, ddepth=-1, kernel=kernel)
    img_conv = Image.fromarray(image_sharp)
    return img_conv
# ----------------- end Sharpening -----------------
