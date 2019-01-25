from PyPDF2 import PdfFileReader
import os
import re
import platform
import csv
from PIL import Image
import colorsys


# python 2.7
class PDF:

    # own policy to try to clean up the text files for better content
    cleanUpParametersForTextFile = ['Vorabfassung - wird durch die endgueltige Fassung ersetzt', '\\', '-',
                                    'Drucksache', 'Deutscher Bundestag', 'Wahlperiode', ' ', '.', '\n', ',',
                                    ':', ';', '(', ')', '[', ']', '?', '!']

    def __init__(self):
        # check which operating system
        if platform.system() == 'Windows':
            self.slashes = '\\'
        else:
            # Linux and OSX
            self.slashes = '/'

        # global parameters both pdf files
        self.path_ungeschwaerzt_pdf = 'pdf_documents' + self.slashes + 'ungeschwaerzt.pdf'
        self.path_ungeschwaerzt_markiert_pdf = 'pdf_documents' + \
            self.slashes + 'ungeschwaerzt_markiert.pdf'

        # txt file path
        self.file_text_ungeschwaerzt_markiert = 'text_files' + \
            self.slashes + 'textfile_ungeschwaerzt_markiert.txt'
        self.file_text_ungeschwaerzt = 'text_files' + \
            self.slashes + 'textfile_ungeschwaerzt.txt'

        # to initiliaze and create both parameter with global variables
        # creating both files and save both in the txt_file folder
        if (not os.path.isfile(self.file_text_ungeschwaerzt) and not not os.path.isfile(self.file_text_ungeschwaerzt_markiert)):
            self.text_ungeschwaerzt = self.text_extractor(
                self.path_ungeschwaerzt_pdf)
            self.text_ungeschwaerzt_markiert = self.text_extractor(
                self.path_ungeschwaerzt_markiert_pdf)

            # store both files as text files
            self.writeAndSaveFile(
                name_of_file='textfile_ungeschwaerzt_markiert', text=self.text_ungeschwaerzt_markiert)
            self.writeAndSaveFile(
                name_of_file='textfile_ungeschwaerzt', text=self.text_ungeschwaerzt)

        else:
            self.text_ungeschwaerzt = open(
                self.file_text_ungeschwaerzt, 'r').read()
            self.text_ungeschwaerzt_markiert = open(
                self.file_text_ungeschwaerzt_markiert, 'r').read()

        self.name_list_from_text_file = []

        # initializing and setting parameter
        self.listOfImages = None
        self.settingListOfimages()

        self.howManyPagesAreMarked = 0
        self.whichPageIsMarked = []



    ''' path: str    
        return value: str '''
    def text_extractor(self, path):
        textWhole = ''
        with open(path, 'rb') as f:
            pdf = PdfFileReader(f)
            for index in range(pdf.getNumPages()):
                page = pdf.getPage(index)
                text = page.extractText().encode('utf-8')
                textWhole += text

        return textWhole

    ''' path: str   
        number: int '''
    def getTextFromPageNumber(self, path='', number=0):
        path_ungeschwaerzt_pdf = 'pdf_documents' + self.slashes + 'ungeschwaerzt.pdf'
        path_ungeschwaerzt_markiert_pdf = 'pdf_documents' + \
            self.slashes + 'ungeschwaerzt_markiert.pdf'

        if path == '':
            path = path_ungeschwaerzt_pdf

        textWhole = ''

        with open(path, 'rb') as f:
            pdf = PdfFileReader(f)
            if pdf.getNumPages() < number:
                raise Exception('We have only ' +
                                str(pdf.getNumPages()) + ' number of pages')
            page = pdf.getPage(number).extractText()

            return page

    ''' target_path: str    
        name_of_file: str   
        text: str '''
    def writeAndSaveFile(self, target_path='', name_of_file='', text=''):
        # 'text_files\\' + 'textfile_ungeschwaerzt_markiert.txt' e.g.
        target_path = 'text_files' + self.slashes
        type_of_file = '.txt'
        text_file = open(target_path + name_of_file + type_of_file, 'w')
        text_file.write(text)

    ''' path: str '''
    def get_info(self, path=''):
        # PDF.path_ungeschwaerzt_markiert_pdf
        # PDF.path_ungeschwaerzt_pdf

        if path == '':
            path = self.path_ungeschwaerzt_pdf

        with open(path, 'rb') as f:
            pdf = PdfFileReader(f)
            info = pdf.getDocumentInfo()
            number_of_pages = pdf.getNumPages()
            author = info.author
            creator = info.creator
            producer = info.producer
            subject = info.subject
            title = info.title
            # For this particular pdf file are no values
            print(author)
            print(producer)
            print(subject)
            print(title)

    ''' automatic for both files and store it into text_files folder
        extraWords: list with elements: str '''
    def cleanUpTextFiles(self, extraWords=[]):
        file_unmarked = open(self.file_text_ungeschwaerzt, 'r')
        file_marked = open(self.file_text_ungeschwaerzt_markiert, 'r')

        text_unmarked = file_unmarked.read()
        text_marked = file_marked.read()

        # remove all elements from our array
        for ele in PDF.cleanUpParametersForTextFile:
            text_unmarked = text_unmarked.replace(ele, '')
            text_marked = text_marked.replace(ele, '')

        # remove the elements for the parameter extraWords
        for ele in extraWords:
            text_unmarked = text_unmarked.replace(ele, '')
            text_marked = text_marked.replace(ele, '')

        # remove numbers form 0 - 9
        for i in range(10):
            text_unmarked = text_unmarked.replace(str(i), "")
            text_marked = text_marked.replace(str(i), "")

        # store both files
        clean_path = 'text_files' + self.slashes
        open(clean_path + "cleantext_text_unmarked.txt", "w").write(text_unmarked)
        open(clean_path + "cleantext_text_marked.txt", "w").write(text_marked)

    ''' very slow maybe with generators '''
    def allNamesFromTextFiles(self):
        list_vornamen = []
        with open('data'+ self.slashes +'alleVornamen.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=' ')
            list_vor = [x[0] for x in csv_reader ]
            list_vornamen = [x for x in set(list_vor) ]

        text = self.text_ungeschwaerzt

        names_in_text = []
       
        words = text.split()

        listi = set(list_vornamen)

        for word in words:
            for name in listi:
                if name == word and (not name in names_in_text):
                    names_in_text.append(name)

        self.name_list_from_text_file = names_in_text

    def settingListOfimages(self):
        for root, dirs, files in os.walk("images"):
            self.listOfImages = files
            # for filename in files:
            #     print(filename)
    
    ''' image search '''
    def calculateForEachImageTheMarkedPart(self):
        for imagePath in self.listOfImages:
            whole_image = 0
            image = Image.open('images' + self.slashes + imagePath).convert('RGBA').resize((64, 64), Image.ANTIALIAS)
            red, orange, yellow, green, turquoise, blue, lilac, pink, white, gray, black, brown = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
            for px in image.getdata():
                whole_image += 1
                h, s, l = colorsys.rgb_to_hsv(px[0]/255., px[1]/255., px[2]/255.)
                h = h * 360
                s = s * 100
                l = l * 100

                if l > 95:
                    white += 1
                elif l < 8:
                    black += 1
                elif s < 8:
                    gray += 1
                elif h < 12 or h > 349:
                    red += 1
                elif h > 11 and h < 35:
                    if s > 70:
                        orange += 1
                    else:
                        brown += 1
                elif h > 34 and h < 65:
                    yellow += 1
                elif h > 64 and h < 150:
                    green += 1
                elif h > 149 and h < 200:
                    turquoise += 1
                elif h > 195 and h < 250:
                    blue += 1
                elif h > 245 and h < 275:
                    lilac += 1
                elif h > 274 and h < 350:
                    pink += 1

            # image is not marked if whole_image == white + gray
            if (float(whole_image) - float(white) - float(gray)) != 0:
                # print(float(yellow) / (float(whole_image) - float(white) - float(gray)))
                # print(gray)
                # print(float(yellow) / (float(gray)))
                # ungeschwaerzt_markiert-0001
                self.howManyPagesAreMarked += 1
                imagePath = imagePath.replace('ungeschwaerzt_markiert-', '')
                number = imagePath.replace('.jpg', '')
                number = int(number)
                self.whichPageIsMarked.append(number)
                

if __name__ == '__main__':
    reader = PDF()
    # reader.writeAndSaveFile(
    #     name_of_file='textfile_ungeschwaerzt_markiert', text=reader.text_ungeschwaerzt_markiert)
    # reader.writeAndSaveFile(
    #     name_of_file='textfile_ungeschwaerzt', text=reader.text_ungeschwaerzt)

    # reader.getTextFromPageNumber(number=1000)
    # reader.get_info()
    # reader.cleanUpTextFiles()
    # reader.allNamesFromTextFiles()
    # print(reader.name_list_from_text_file)
    
    reader.calculateForEachImageTheMarkedPart()
    

    print(reader.howManyPagesAreMarked)
    print(reader.whichPageIsMarked)

    with open('testFile.txt', 'w') as f:
        for item in reader.whichPageIsMarked:
            f.write("%s\n" % item)

