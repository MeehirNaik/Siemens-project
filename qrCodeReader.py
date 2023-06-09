# from pyzbar import pyzbar
# import cv2

# img_path = r"C:\Users\naikm\Downloads\A-QR-code-based-paper-ticket-of-the-Delhi-Metro---_1683570054247.webp"

# image = cv2.imread(img_path)

# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# barcodes = pyzbar.decode(gray)

# for barcode in barcodes:
#     qr_code_data = barcode.data.decode("utf-8")
#     qr_code_type = barcode.type
#     print("QR Code:", qr_code_data)
#     print("Type:", qr_code_type)


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
        
        # codes = read_codes_from_image(gray)
        codes = decode(gray)
        
        # Display the results
        if len(codes) > 0:

            

            for barcode in codes:
                qr_code_data = barcode.data.decode("utf-8")
                qr_code_type = barcode.type
                print("QR Code:", qr_code_data)
                print("Type:", qr_code_type)
        else:
            print("No codes found in the image.")
        
# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()
