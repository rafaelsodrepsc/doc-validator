from services.preprocessor import pre_process
from services.ocr_service import ocr_service
from services.extractor import extract

image_path = 'samples/documento.png'

pre_processment = pre_process(image_path)

ocr = ocr_service(pre_processment)

print(extract(ocr))