import qrcode

input_data = "https://github.com/isanjayrassani"

qr = qrcode.QRCode(
    version = 15,
    box_size = 10,
    border = 5
)


qr.add_data(input_data)
qr.make(fit = True)

img = qr.make_image(fill="black", back_color="white")
img.save("test.png")