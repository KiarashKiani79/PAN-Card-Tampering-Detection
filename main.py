# import the necessary packages
import os
from skimage.metrics import structural_similarity
import imutils
import cv2
from PIL import Image
import requests

# Create directories for storing images
os.makedirs("pan_card_tampering", exist_ok=True)
os.makedirs("pan_card_tampering/image", exist_ok=True)

# Open image and display
original = Image.open(requests.get('https://www.thestatesman.com/wp-content/uploads/2019/07/pan-card.jpg', stream=True).raw)
tampered = Image.open(requests.get('https://assets1.cleartax-cdn.com/s/img/20170526124335/Pan4.png', stream=True).raw)

# Print image size
print("Original Image size: " + str(original.size))
print("Tampered Image size: " + str(tampered.size))

# Print image format
print("Original Image format: " + original.format)
print("Tampered Image format: " + tampered.format)
print("-----------------------------------")

# Resize image
original = original.resize((250,160))
print("Resized Origninal Image size: " + str(original.size))
original.save("pan_card_tampering/image/original.png")

tampered = tampered.resize((250,160))
print("Resized Tampered Image size: " + str(tampered.size))
original.save("pan_card_tampering/image/tampered.png")
print("-----------------------------------")