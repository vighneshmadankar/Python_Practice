import qrcode
from PIL import Image
import qrcode.constants

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=11,border=4,)
qr.add_data(input("ADD TEXT OR LINK : "))
img = qr.make_image(fill_color=input("Enter Color :"), back_color=input("Enter Color :"))
img.save(input("Enter filename :"))
