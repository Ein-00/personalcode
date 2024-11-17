
import qrcode

# Data to be encoded
data = "16ee952898cc860d47368383950474472c69ba412a2a95ba922128042b6dfa91aa7cca1c0ecfafaf9991d2cc2fc53abc813c54b3dffa1a76e811d819c3a32c4cdb1218394e74ce1be0329b7160441484171c217beb91141c1f9e6a4855c46facf0fb48d15609a4597bc57ce62e3908c91af514de610a64115f3426bc58377559ca89ecd4f15b2c14e6465656c77586e48ce6a4877460074ebb4fb89c6ae139f65164279aff1ef1d24f77d57506a7f15d9f395c04256202e243d38b501581d375dafc3d893b6dd4363976d4032709f54db8489d8faa3d82f84065322fa8f9ea2abe1d22d99f00ded617d1b5c25eb37a2279903c61edcb33e7c277670f5ef3f7ea"

# Create a QR Code instance
qr = qrcode.QRCode(
    version=1,  # controls the size of the QR Code
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # controls the error correction used for the QR Code
    box_size=10,  # controls how many pixels each “box” of the QR code is
    border=4,  # controls how many boxes thick the border should be
)

# Add data to the QR Code
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("qrcode.png")

print("QR Code generated and saved as 'qrcode.png'")

