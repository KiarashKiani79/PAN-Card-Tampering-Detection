## PAN Card Tampering Detection

This project explores a basic approach to detecting potential tampering in PAN cards using image processing techniques. It leverages the Structural Similarity Index Measure (SSIM) and contour analysis to identify areas of dissimilarity between an original PAN card image and a potentially tampered version.

**Important Note:** This is an educational project and should not be used for real-world PAN card verification due to potential limitations. For reliable verification methods, consult with financial or security professionals.

**Functionality:**

* **Image Processing:** Loads, resizes, and converts images to grayscale for analysis.
* **SSIM Calculation:** Computes the SSIM score to measure the structural similarity between the images.
* **Difference Image Generation:** Creates a difference image highlighting areas of dissimilarity.
* **Thresholding and Contours:** Applies thresholding to create a binary image emphasizing potential tampering regions. Finds contours within these regions.

**Implementation Details (Commented Out):**

* The code initially included file system operations (creating directories and saving images) but is commented out as reusable code generally avoids such dependencies.
* Downloading images from URLs is also commented out due to security concerns. Consider using local file paths for your PAN card images.

**Running the Project:**

1. Save the code as a Python file (e.g., `pan_card_tampering_detector.py`).
2. Place your PAN card images (original and tampered) in the same directory as the script.
3. Run the script from the command line: `python pan_card_tampering_detector.py`
4. The script will process the images and display the SSIM score in the console, indicating the level of structural similarity.

**Project Limitations:**

* This approach might not be robust for real-world scenarios and requires further enhancements.
* More sophisticated techniques (machine learning) might be necessary for robust tampering detection.
* The code doesn't account for legitimate modifications to PAN cards (e.g., name changes).

**Further Considerations:**

* Explore pre-trained models for PAN card tampering detection if SSIM and contours prove insufficient.
* Investigate image preprocessing techniques like noise reduction and sharpening to improve accuracy.
* Implement unit tests to ensure code functionality.

<div style="display: flex; align-items: center;">
  <img src="https://github.com/KiarashKiani79/PAN-Card-Tampering-Detection/blob/main/pan_card_tampering/image/original.png" width="400" style="margin-right: 10px;" />
  <div style="background-color: lightgray; padding: 5px; font-size: 12px;">Original Image</div>
  
  <img src="https://github.com/KiarashKiani79/PAN-Card-Tampering-Detection/blob/main/pan_card_tampering/image/tampered.png" width="400" style="margin-right: 10px;" />
  <div style="background-color: lightgray; padding: 5px; font-size: 12px;">Tampered Image</div>

  <img src="https://github.com/KiarashKiani79/PAN-Card-Tampering-Detection/blob/main/pan_card_tampering/image/original_contoured.png" width="400" style="margin-right: 10px;" />
  <div style="background-color: lightgray; padding: 5px; font-size: 12px;">Original Image with Contour</div>

  <img src="https://github.com/KiarashKiani79/PAN-Card-Tampering-Detection/blob/main/pan_card_tampering/image/tampered_contoured.png" width="400" style="margin-right: 10px;" />
  <div style="background-color: lightgray; padding: 5px; font-size: 12px;">Tampered Image with Contour</div>

  <img src="https://github.com/KiarashKiani79/PAN-Card-Tampering-Detection/blob/main/pan_card_tampering/image/diff.png" width="400" style="margin-right: 10px;" />
  <div style="background-color: lightgray; padding: 5px; font-size: 12px;">Difference Image with Black</div>

  <img src="https://github.com/KiarashKiani79/PAN-Card-Tampering-Detection/blob/main/pan_card_tampering/image/thresh.png" width="400" style="margin-right: 10px;" />
  <div style="background-color: lightgray; padding: 5px; font-size: 12px;">Threshold Image with White</div>
</div>
