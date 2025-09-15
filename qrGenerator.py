import qrcode
input_data = input("Enter the data to encode in the QR code (in url): ").strip()
input_filename = input("Enter the filename : ").strip()
if not input_filename.lower().endswith(".png"):
    input_filename += ".png"
qr = qrcode.QRCode(box_size=10, border=5)
qr.add_data(input_data)
img = qr.make_image(fill_color="black", back_color="white")
img.save(input_filename)
print(f"QR code saved as {input_filename}")
