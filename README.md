# Siemens-project
all files

import cv2
from pyzbar.pyzbar import decode

def read_codes_from_image(image):
    # Decode the codes
    codes = decode(image)
    
    # Extract and return the data from the codes
    results = []
    for code in codes:
        data = code.data.decode('utf-8')
        barcode_type = code.type
        results.append((data, barcode_type))
    
    return results

# Initialize the webcam
cap = cv2.VideoCapture(0)

while True:
    # Capture frame from the webcam
    ret, frame = cap.read()
    
    # Display the captured frame
    cv2.imshow('Webcam', frame)
    
    # Wait for key press
    key = cv2.waitKey(1)
    
    # Press 'q' to quit the program
    if key == ord('q'):
        break
    
    # Press 's' to capture and process the current frame
    if key == ord('s'):
        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Read the codes from the frame
        codes = read_codes_from_image(gray)
        
        # Display the results
        if len(codes) > 0:
            print("Found codes:")
            for code in codes:
                data, barcode_type = code
                print("Type:", barcode_type)
                print("Data:", data)
        else:
            print("No codes found in the image.")
        
# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()
