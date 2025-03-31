import qrcode
from qrcode.image.pure import PyPNGImage


data = input("Enter the text or URL: ").strip()
filename = input("Enter the file name: ").strip()

if not filename.endswith('.png'):
    filename += '.png'

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)

image = qr.make_image(fill_color = 'black', back_color = 'white', image_factory=PyPNGImage)
image.save(filename)

print(f'QR code saved as {filename}')















