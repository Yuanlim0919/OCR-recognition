#-*- coding: utf-8 -*-

from pdf2image import convert_from_bytes

pdf_file = 'C:\pdf_recog\Historic_data2007.pdf'
pages = convert_from_bytes(open(pdf_file,'rb').read())
image_path = 'C:\pdf_recog\Data 2007'
image_counter = 1

for page in pages:
    
    filename = image_path+"\page_"+str(image_counter)+".png"
    page.save(filename,'PNG')
    image_counter +=1

