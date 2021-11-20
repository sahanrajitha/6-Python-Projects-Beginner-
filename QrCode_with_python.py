import qrcode

data = 'Don\'t forget to subscride'

qr = qrcode.QRCode(version = 1,box_size=10,border=5)

qr.add_data(data)

qr.make(fit=True)
img = qr.make_image(fill_color='red',back_color='white')

img.save('E:/notepad ++ projects/6 python projects in freecodecamp video/qrcode photos/qrcode.png')
