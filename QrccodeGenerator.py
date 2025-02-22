import qrcode as qr
img= qr.make(input("Enter Text For qr :"))
img.save(input("Enter Filename :"))
