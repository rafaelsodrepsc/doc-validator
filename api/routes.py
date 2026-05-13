from services.preprocessor import pre_process
from services.ocr_service import ocr_service
from services.extractor import extract
from fastapi import APIRouter, UploadFile,HTTPException
import numpy as np
from io import BytesIO
import cv2

router = APIRouter()

@router.post("/validar")
async def upload_file(file: UploadFile):
    try:
        content = await file.read()
        
        buffer = BytesIO(content)
        array = np.frombuffer(buffer.getvalue(), dtype=np.uint8)
        image = cv2.imdecode(array, cv2.IMREAD_COLOR)
        
        if image is None:
            raise HTTPException(status_code=400, detail="Arquivo inválido ou não é uma imagem")
        
        result = extract(ocr_service(pre_process(image)))
        return result
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro no processamento: {str(e)}")