import PyPDF2
import textract

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


filename = 'hp.pdf'

pdfFileObj = open('hp.pdf','rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

num_pages = pdfReader.num_Pages
count = 14
text = ""

while count < num_pages:
    pageObj = pdfReader.getPage(count)
    count +=1
    text += pageObj.extractText ()

if text != "":
    text = text

else:
    text =textract.process(hp.pdf,method='tesseract',language='eng')




print (text)