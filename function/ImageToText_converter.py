import pytesseract
from PIL import Image
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
img = Image.open("../numbers.jpg")
text = pytesseract.image_to_string(img)

print(text)


# reference need to update
# sudo apt update
# sudo apt install tesseract-ocr
# sudo apt install libtesseract-dev