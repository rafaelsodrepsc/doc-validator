import cv2

def pre_process(image_path):
    image = cv2.imread(image_path)

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    ret, img_thres = cv2.threshold(gray_image, 127,255, cv2.THRESH_BINARY)

    return img_thres