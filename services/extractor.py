import re

def extract(text):
    name = re.search(r'(?<=Nome: ).+',text)
    cpf = re.search(r'\d{3}.\d{3}.\d{3}-\d{2}',text)
    date = re.search(r'\d{2}/\d{2}/\d{4}',text)
    
    return {
        "nome": name.group() if name else None,
        "cpf": cpf.group() if cpf else None,
        "data": date.group() if date else None
    }
    