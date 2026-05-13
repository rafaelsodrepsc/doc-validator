from services import extract,ocr_service,preprocess

image_path = 'samples/documento.png'

pre_processment = preprocess(image_path)

ocr = ocr_service(pre_processment)

print(extract(ocr))