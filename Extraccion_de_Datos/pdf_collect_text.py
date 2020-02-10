'''reading and extract text from pdfs using python PyPDF2 library'''
#pip install PyPDF2

#import external libraries
import PyPDF2

#import modules from library
from PyPDF2 import PdfFileReader

#download any pdf file and place it in the location where you are running this script

#creating a pdf file object
pdf=open("file.pdf","rb")

#create pdf reader object
pdf_reader=PyPDF2.PdfFileReader(pdf)

#checking num pages
print(pdf_reader.numPages)

#creating a page object
page =pdf_reader.getPage(0)

#extracting text from the page!
print(page.extractText())

#closing the pdf file
pdf.close()
