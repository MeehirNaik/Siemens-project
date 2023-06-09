# # Haris corner detection

# # Importing the libraries
# import cv2
# import numpy as np
  
# # Reading the image and converting the image to B/W
# image = cv2.imread('surfObjectDetection\WIN_20230601_20_44_55_Pro.jpg')
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# gray_image = np.float32(gray_image)
  
# # Applying the function
# dst = cv2.cornerHarris(gray_image, blockSize=2, ksize=3, k=0.04)
  
# # dilate to mark the corners
# dst = cv2.dilate(dst, None)
# image[dst > 0.01 * dst.max()] = [0, 255, 0]
  
# cv2.imshow('haris_corner', image)
# cv2.waitKey()


# # Shi-Tomasi corner detection

# # Importing the libraries
# import cv2
# import numpy as np
  
# # Reading the image and converting into B?W
# image = cv2.imread('surfObjectDetection\WIN_20230601_20_44_55_Pro.jpg')
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  
# # Applying the function
# corners = cv2.goodFeaturesToTrack(
#     gray_image, maxCorners=50, qualityLevel=0.02, minDistance=20)
# corners = np.float32(corners)
  
# for item in corners:
#     x, y = item[0]
#     x = int(x)
#     y = int(y)
#     cv2.circle(image, (x, y), 6, (0, 255, 0), -1)
  
# # Showing the image
# cv2.imshow('good_features', image)
# cv2.waitKey()



# # FAST algorithm for corner detection

# # Importing the libraries
# import cv2
  
# # Reading the image and converting into B/W
# image = cv2.imread('surfObjectDetection\WIN_20230601_20_44_55_Pro.jpg')
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  
  
# # Applying the function
# fast = cv2.FastFeatureDetector_create()
# fast.setNonmaxSuppression(False)
  
  
# # Drawing the keypoints
# kp = fast.detect(gray_image, None)
# kp_image = cv2.drawKeypoints(image, kp, None, color=(0, 255, 0))
  
# cv2.imshow('FAST', kp_image)
# cv2.waitKey()



# ORB (Oriented FAST and Rotated Brief)

# Importing the libraries
import cv2
  
# Reading the image and converting into B/W
image = cv2.imread('surfObjectDetection\WIN_20230601_20_44_55_Pro.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  
# Applying the function
orb = cv2.ORB_create(nfeatures=2000)
kp, des = orb.detectAndCompute(gray_image, None)
  
# Drawing the keypoints
kp_image = cv2.drawKeypoints(image, kp, None, color=(0, 255, 0), flags=0)
  
cv2.imshow('ORB', kp_image)
cv2.waitKey()