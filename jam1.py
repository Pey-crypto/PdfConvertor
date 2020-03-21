

import PyPDF2
import textract

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords





#Write a for-loop to open many files (leave a comment if you'd like to learn how).
filename = 'hp.pdf' 
#open allows you to read the file.
pdfFileObj = open('hp.pdf','rb')
#The pdfReader variable is a readable object that will be parsed.
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
#Discerning the number of pages will allow us to parse through all the pages.
num_pages = pdfReader.numPages
count = 4
text = ""
#The while loop will read each page.
while count < num_pages:
    pageObj = pdfReader.getPage(count)
    count +=1
    text += pageObj.extractText()
#This if statement exists to check if the above library returned words. It's done because PyPDF2 cannot read scanned files.
if text != "":
   text = text
#If the above returns as False, we run the OCR library textract to #convert scanned/image based PDF files into text.
else:
   text = textract.process('hp.pdf', method='tesseract', language='eng')

print (text)