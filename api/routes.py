from services.preprocessor import pre_process
from services.ocr_service import ocr_service
from services.extractor import extract
from fastapi import APIRouter, UploadFile
import numpy as np
from io import BytesIO
import cv2

router = APIRouter()

@router.post("/validar")
async def upload_file(file: UploadFile):
    content = await file.read()
    
    buffer = BytesIO(content)
    array = np.frombuffer(buffer.getvalue(), dtype=np.uint8)
    image = cv2.imdecode(array, cv2.IMREAD_COLOR)

    image_treat = extract(ocr_service(pre_process(image)))
    
    return image_treat