# extracting_text.py
from PyPDF2 import PdfFileReader
def text_extractor(path):
    textWhole = ''
   
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
       
        page = pdf.getPage(128)
        print(page)
        print('--------------------------------------------------------------------------')
        print('--------------------------------------------------------------------------')
        print('Page type: {}'.format(str(type(page))))
        print('--------------------------------------------------------------------------')
        print('--------------------------------------------------------------------------')
        text = page.extractText().encode('utf-8')# '\xea\x80\x80abcd\xde\xb4' #.encode("ascii", "ignore")
        textWhole += text
        print(text)
        


    return textWhole

if __name__ == '__main__':
    path = 'ungeschwaerzt.pdf'
    text = text_extractor(path)#.encode("ascii", "ignore")

    file = open('testFile.txt','w') 
    file.write(text) 