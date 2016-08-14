# Make sure we already installed PIL and tesseract-ocr

from PIL import Image
import pytesseract

print(pytesseract.image_to_string(Image.open("test.png")))