from PIL import Image, ImageDraw,ImageFont

font = ImageFont.truetype("arial.ttf", size=24)

img = Image.new('RGB',(400,200), color=(255,255,255))

draw = ImageDraw.Draw(img)

draw.text((50,50), "Nome: Rafael Sodre Paschoal",fill=(0,0,0),font=font)
draw.text((50,90), "CPF: 123.456.789-09",fill=(0,0,0),font=font)
draw.text((50,130), "Data de Nascimento: 09/09/2003",fill=(0,0,0),font=font)

img.show()
img.save('samples/documento.png')