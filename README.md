# Doc Validator

API de validação de documentos via OCR, extrai e valida campos de imagens via upload.

## Stack

- Python + FastAPI
- OpenCV (pré-processamento)
- Tesseract (OCR)
- Regex (extração de campos)

## Instalação

```bash
pip install fastapi uvicorn python-multipart opencv-python pytesseract Pillow numpy
```

Instalar Tesseract: https://github.com/UB-Mannheim/tesseract/wiki

## Rodando

```bash
uvicorn main:app --reload
```

## Uso

`POST /validar` -> envia uma imagem de documento e retorna os campos extraídos.

Acesse `http://localhost:8000/docs` para testar via Swagger.

## Exemplo de resposta

```json
{
  "nome": "Rafael Sodre Paschoal",
  "cpf": "123.456.789-09",
  "data": "09/09/2003"
}
```