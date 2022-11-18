import numpy as np
import pywt
import cv2
from scipy.fft import fft, ifft
from scipy import signal

def main():
    filePath = "C:/Users/vscha/Documents/USM/2022-2/pdi_real/proyecto"
    cap = cv2.VideoCapture(filePath + "/data/2022_08_05_06_00_00.mkv")
    if (cap.isOpened()== False): 
        print("Error opening video stream or file")
 
    # Read until video is completed
    while(cap.isOpened()):
    # Capture frame-by-frame
        ret, frame = cap.read()
        if ret == True:
        
            histogramas = w2d(frame)
            
            
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            c = 255 / np.log(1 + np.max(gray))
            log_image = c * (np.log(gray + 1))
            log_image = np.array(log_image, dtype = np.uint8)
            
            # Specify the data type so that
            # float value will be converted to int

            fast_fourier_transform = fft(log_image)
            sos = signal.butter(10, 15, 'hp', fs=1000, output='sos')
            filtered = signal.sosfilt(sos, fast_fourier_transform)
            inverse_transform = ifft(filtered)
            
            result_image_after_filter = np.exp(inverse_transform * (np.log(256)) / 255) - 1
            result_image_after_filter = np.array(result_image_after_filter, dtype = np.uint8)

            vis = cv2.cvtColor(result_image_after_filter, cv2.COLOR_GRAY2BGR)
            vis_gray = cv2.cvtColor(vis, cv2.COLOR_BGR2GRAY)

            cv2.imshow('Frame',vis_gray)
            #break

            # Press Q on keyboard to  exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        
        # Break the loop
        else: 
            break
 
# When everything done, release the video capture object
    cap.release()
 
# Closes all the frames
cv2.destroyAllWindows()

def w2d(img, mode='haar', level=1):
    imArray = img
    
    #Datatype conversions
    #convert to grayscale
    imArray = cv2.cvtColor( imArray,cv2.COLOR_RGB2GRAY )
    
    #convert to float
    imArray =  np.float32(imArray)   
    imArray /= 255
    
    # compute coefficients 
    coeffs = pywt.wavedec2(imArray, mode, level=level)

    #Process Coefficients
    coeffs_H = list(coeffs)  
    coeffs_H[0] *= 0 

    # reconstruction
    imArray_H = pywt.waverec2(coeffs_H, mode)
    imArray_H *= 255
    imArray_H = np.uint8(imArray_H)

    return imArray_H

if __name__ == "__main__":
    main()