import qrcode
from qrcode.image.pure import PyPNGImage
import tkinter as tk
from tkinter import colorchooser


data = input("Enter the text or URL: ").strip()
filename = input("Enter the file name: ").strip()

if not filename.endswith('.png'):
    filename += '.png'


qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)

qr.make(fit=True)


root = tk.Tk() #Create main window
root.withdraw() #Hide window right after choose

fill_color = colorchooser.askcolor(title = "Choose color")[1]
back_color = colorchooser.askcolor(title = "Choose color")[1]

image = qr.make_image(fill_color = fill_color, back_color = back_color, image_factory=PyPNGImage)
image.save(filename)

print(f'QR code saved as {filename}')
















