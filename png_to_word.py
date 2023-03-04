#-*- coding: utf-8 -*-

from PIL import Image
import pytesseract
import pandas as pd

writer = pd.ExcelWriter('1983.xlsx',engine='xlsxwriter')
month = ['Jan','Feb','Mar','Apr','May','June','July','Aug','Sep','Oct','Nov','Dec']
a = 12*22

for i in range(12):
    img_path = 'C:\pdf_recog\pdf_image\data\page_'+str(23+i+a)+'.png'

    img = Image.open(img_path)

    word01 = pytesseract.image_to_string(img,lang='eng')
    word01 = word01.split("\n")
    
    j = 9
    data =[]
    while j <=40:
        ext = word01[j].split(" ")
        data.append(ext)
        j+=1

    output = pd.DataFrame(data)
    output.to_excel(writer,sheet_name = month[i])

writer.save()

