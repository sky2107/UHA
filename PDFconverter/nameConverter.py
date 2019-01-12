# extracting_text.py
from PyPDF2 import PdfFileReader
def text_extractor(path):
    textWhole = ''
    count = 0
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        # get the first page
        # print(pdf.getNumPages())
        for index in range(pdf.getNumPages()):
            page = pdf.getPage(index)
            # print(page)
            # print('Page type: {}'.format(str(type(page))))
            text = page.extractText()# .encode('utf-8')
            textWhole += text
            # print(text)
            
    return textWhole

if __name__ == '__main__':
    file_names = 'vornamen.pdf'
    
    text_names = text_extractor(file_names).encode('utf-8')
    
    file_text_names = open('vornamen.txt','w') 
   

    file_text_names.write(text_names) 
    