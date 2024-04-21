# import the necessary packages
import subprocess
from skimage.metrics import structural_similarity
import imutils
import cv2
from PIL import Image
import requests


subprocess.run(["mkdir", "pan_card_tampering"])
subprocess.run(["mkdir", "pan_card_tampering/image"])

# Open image and display
original = Image.open(requests.get('https://www.thestatesman.com/wp-content/uploads/2019/07/pan-card.jpg', stream=True).raw)
tampered = Image.open(requests.get('https://assets1.cleartax-cdn.com/s/img/20170526124335/Pan4.png', stream=True).raw) 

