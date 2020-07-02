# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 12:18:32 2018

@author: Jorge
"""

import os
import PyPDF2
from PyPDF2 import PdfFileReader
from StringIO import StringIO
import unidecode

os.chdir("E:\\datam\\Peru\\Politica\\peruano")
#os.chdir("E:\\databulk\\peru\\politica")

# Function to get text from PDF
def getPDFContent(path, pages=[]):
    content = ""
    p = file(path, "rb")
    pdf = PyPDF2.PdfFileReader(p)
    if pages:
        for i in pages:
            content += pdf.getPage(i).extractText() + "\n"
    else:
        numPages = pdf.getNumPages()
        for i in range(numPages):
            content += pdf.getPage(i).extractText() + "\n"
    content = " ".join(content.replace(u"\xa0", " ").strip().split())
    return content

# Get number of pages
pdf = PdfFileReader(open('normas/20000102.pdf','rb'))
npages = pdf.getNumPages()

# Read columns (2 per page)
out = getPDFContent('normas/20000102.pdf',pages=[0,npages-1])
#a es \xe1 #e es \xe9 #i es \xed #o es \xf3 #u es \xda #n es \xf1 

out2 = unidecode.unidecode(out)
out2 = out2.replace('- ','')
out2 = out2.replace('-','')
# Find position in string
keyword = 'Designar a partir de la fecha al'
print(out2.find(keyword))
if out2.find(keyword) > -1:
    pos = out2.find(keyword) + len(keyword) + 1
    substring =  out2[pos:]
    posfin = substring.find(',')
    name = substring[0:posfin]




