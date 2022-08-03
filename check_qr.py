import qrcode

input_data = 'https://github.com/isanjayrassani'

qr = qrcode.QRCode(
    # The version parameter is an integer from 1 to 40 that controls the size of the QR Code (the smallest, version 1, is a 21x21 matrix). Set to None and use the fit parameter when making the code to determine this automatically.
    version = 15,
    # The box_size parameter controls how many pixels each “box” of the QR code is.
    box_size = 10,
    # The border parameter controls how many boxes thick the border should be (the default is 4, which is the minimum according to the specs).
    border = 5
)


qr.add_data(input_data)
qr.make(fit = True)

# fill_color and back_color can change the background and the painting color of the QR, when using the default image factory. Both parameters accept RGB color tuples.
img = qr.make_image(fill="black", back_color="white")

img.save('test.png')
