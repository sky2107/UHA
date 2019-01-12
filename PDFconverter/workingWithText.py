import re


file_marked = open('textfile_ungeschwaerzt.txt', 'r')
text = file_marked.read()
file_marked.close()
file_unmarked = open('textfile_ungeschwaerzt_markiert.txt', 'r')

text1 = file_unmarked.read()

text = text.replace("Vorabfassung - wird durch die endgueltige Fassung ersetzt", "")
text1 = text1.replace("Vorabfassung - wird durch die endgueltige Fassung ersetzt", "")

text = text.replace("\\", "")
text1 = text1.replace("\\", "")

text = text.replace("-", "")
text1 = text1.replace("-", "")

text = text.replace("Drucksache", "")
text1 = text1.replace("Drucksache", "")

text = text.replace("Deutscher Bundestag", "")
text1 = text1.replace("Deutscher Bundestag", "")

text = text.replace("Wahlperiode", "")
text = text.replace("Wahlperiode", "")

text = text.replace(" ", "")
text = text.replace(".", "")

text1 = text1.replace(" ", "")
text1 = text1.replace(".", "")

text = text.replace("\n", "")
text1 = text1.replace("\n", "")

text = text.replace(",", "")
text1 = text1.replace(",", "")

text = text.replace("(", "")
text1 = text1.replace("(", "")

text = text.replace(")", "")
text1 = text1.replace(")", "")

text = text.replace("[", "")
text1 = text1.replace("]", "")

text = text.replace(":", "")
text1 = text1.replace(":", "")

text = text.replace(";", "")
text1 = text1.replace(";", "")

text = text.replace("?", "")
text1 = text1.replace("?", "")

print(type(text))

print(len(text))
print(len(text1))

for i in range(10):
    text = text.replace(str(i), "")
    text1 = text1.replace(str(i), "")



pattern = re.compile(r'X')

matches = pattern.finditer(text)
count = 0
for match in matches:
    count += 1
    # print(match.span()[0])
    # print(text[match.span()[0]-100:match.span()[1]+10])

print(count)
print(len(text))
print(float(count)/float(len(text)))

matches = pattern.finditer(text1)
count = 0
for match in matches:
    count += 1
print(count)
print(len(text1))
print(float(count)/(float(len(text1) - float(16000))))

file = open("cleantext.txt", "w")

file.write(text1)