import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def ocr_service(img_thres):
    text = pytesseract.image_to_string(img_thres)
    
    return text