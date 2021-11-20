from pyzbar.pyzbar import decode
from PIL import Image

img = img.open('E:/notepad ++ projects/6 python projects in freecodecamp video/qrcode photos/qrcode.png')

result = decode(img)

print(result)
