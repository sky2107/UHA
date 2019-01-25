# extracting_text.py
from PyPDF2 import PdfFileReader
def text_extractor(path):
    textWhole = ''
    count = 0
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        # get the first page
        print(pdf.getNumPages())
        for index in range(pdf.getNumPages()):
            page = pdf.getPage(index)
            # print(page)
            # print('Page type: {}'.format(str(type(page))))
            text = page.extractText().encode('utf-8')
            textWhole += text
            # print(text)
            count += 1
            print(count)

    return textWhole

if __name__ == '__main__':
    path_ungeschwaerzt = 'ungeschwaerzt.pdf'
    path_ungeschwaerzt_markiert = 'ungeschwaerzt_markiert.pdf'
    text_ungeschwaerzt_markiert = text_extractor(path_ungeschwaerzt_markiert).encode('utf-8')# .encode("ascii", "ignore")
    text_ungeschwaerzt = text_extractor(path_ungeschwaerzt).encode('utf-8')
    
    file_ungeschwaerzt_markiert = open('textfile_ungeschwaerzt_markiert.txt','w') 
    file_ungeschwaerzt = open('textfile_ungeschwaerzt.txt','w') 

    file_ungeschwaerzt.write(text_ungeschwaerzt) 
    file_ungeschwaerzt.write(text_ungeschwaerzt)

    file_ungeschwaerzt_markiert.write(text_ungeschwaerzt_markiert) 
    file_ungeschwaerzt_markiert.write(text_ungeschwaerzt_markiert)
