import cv2
import numpy as np

def enhance_image(image):
    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply histogram equalization
    equalized_image = cv2.equalizeHist(gray_image)

    # Apply Gaussian blur
    blurred_image = cv2.GaussianBlur(equalized_image, (5, 5), 0)

    # Apply sharpening using unsharp masking
    unsharp_image = cv2.addWeighted(equalized_image, 1.5, blurred_image, -0.5, 0)

    return unsharp_image

def capture_images():
    cap = cv2.VideoCapture(0)  # Open the webcam (change the parameter if using a different camera)
    ret, frame = cap.read()

    cv2.imshow('Processed Image', frame)
    cv2.waitKey(5000)  # Display each image for 1 second

    cap.release()  # Release the webcam

    return frame

def process_images(images):
    processed_images = []
    for image in images:
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert image to grayscale
        enhanced_image = cv2.equalizeHist(gray_image)  # Apply histogram equalization for high contrast
        processed_images.append(enhanced_image)

    return processed_images

def display_images(image):
    cv2.imshow('Processed Image', image)
    cv2.waitKey(5000)  # Display each image for 1 second
    cv2.destroyAllWindows()

# Capture 10 images
num_images = 10
captured_images = capture_images()

processed_images = enhance_image(captured_images)

# Display the processed images
display_images(processed_images)
