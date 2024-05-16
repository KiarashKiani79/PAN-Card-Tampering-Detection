# import the necessary packages
import os
from skimage.metrics import structural_similarity
import imutils
import cv2
from PIL import Image
import requests

# Create directories for storing images
#* os.makedirs("pan_card_tampering", exist_ok=True)
#* os.makedirs("pan_card_tampering/image", exist_ok=True)

# Open image and display
original = Image.open(requests.get('https://www.thestatesman.com/wp-content/uploads/2019/07/pan-card.jpg', stream=True).raw)
tampered = Image.open(requests.get('https://assets1.cleartax-cdn.com/s/img/20170526124335/Pan4.png', stream=True).raw)

#? Original Image size: (1200, 800)
#? Tampered Image size: (282, 179)
#? Original Image format: JPEG
#? Tampered Image format: PNG
#? -----------------------------------

# Resize image
original = original.resize((250,160))
tampered = tampered.resize((250,160))

#* original.save("pan_card_tampering/image/original.png")
#* tampered.save("pan_card_tampering/image/tampered.png")
# ?Resized Origninal Image size: (250, 160)
# ?Resized Tampered Image size: (250, 160)
# ?-----------------------------------

# load the two input images and convert them to matrices
original = cv2.imread("pan_card_tampering/image/original.png")
tampered = cv2.imread("pan_card_tampering/image/tampered.png")

# Convert the images to grayscale
original_gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
tampered_gray = cv2.cvtColor(tampered, cv2.COLOR_BGR2GRAY)

# Compute the Structural Similarity Index (SSIM) between the two images, ensuring that the difference image is returned
(score, diff) = structural_similarity(original_gray, tampered_gray, full=True)
#scaling the difference map to 8-bit grayscale values.
diff = (diff * 255).astype("uint8")
# ?SSIM: SSIM: 0.31686135690489126
# ?diff.shape: (160, 250)

# Calculating threshold and contours 
thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

# loop over the contours
for c in cnts:
    # applying contours on image
    (x, y, w, h) = cv2.boundingRect(c)
    cv2.rectangle(original, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.rectangle(tampered, (x, y), (x + w, y + h), (0, 0, 255), 2)
    
#save original / tampered image with contour in the output directory
#* cv2.imwrite("pan_card_tampering/image/original_contoured.png", original)
#* cv2.imwrite("pan_card_tampering/image/tampered_contoured.png", tampered)

