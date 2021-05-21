from PIL import Image
from pyzbar.pyzbar import decode
data = decode(Image.open("qrSOLVE.png"))
print(data)