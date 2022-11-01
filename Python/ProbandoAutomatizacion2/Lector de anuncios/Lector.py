# from pytesseract import pytesseract
import cv2

tesse_rut = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
#pytesseract.tesseract_cmd = tesse_rut


def lector():
    img_rut = "D:\Personal_Projects\Python\ProbandoAutomatizacion2"

    img = cv2.imread(img_rut)

    #txt = pytesseract.image_to_string(img)


def main():
    return 0
