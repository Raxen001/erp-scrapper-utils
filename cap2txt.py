import cv2
from pytesseract import image_to_string
import requests
import sys

def cap2txt(png):
    img = cv2.imread(png)



    gry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    (h, w) = gry.shape[:2]
    gry = cv2.resize(gry, (w*2, h*2))
    cls = cv2.morphologyEx(gry, cv2.MORPH_CLOSE, None)
    thr = cv2.threshold(cls, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    txt = image_to_string(thr)
    txt = txt.replace(" ", "")
    txt = txt.replace("\n", "")


    #debug
    print('captcha: ', txt)
    cv2.imshow("captcha", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(0)

    return txt
