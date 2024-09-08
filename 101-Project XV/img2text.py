# pip install tesseract

import pytesseract
import os 
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"D:\vs code\my_folder\python\Modules\tesseract.exe" # path to tesseract

def convert() :
    img  = Image.open('ocr_img1.png')
    text = pytesseract.image_to_string(img)
    print(text)
    
convert()   
