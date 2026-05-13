from PIL import Image, ImageDraw

img = Image.new('RGB',(400,200), color=(255,255,255))

draw = ImageDraw.Draw(img)

draw.text((50,50), "Nome: Rafael Sodre Paschoal",fill=(0,0,0))
draw.text((50,70), "CPF: 123.456.789-09",fill=(0,0,0))
draw.text((50,90), "Data de Nascimento: 09/09/2003",fill=(0,0,0))

img.show()
img.save('documento.png')