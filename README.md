# UHA

Urban Hacking
Informatik Projekt

Felix Navas 1412100
Jonas Lagaude 1430596
Ahmed Warsame 1611148

requirements for this code base 
python 2.7 
libaries => PyPDF2, os, re, platform, PIL, colorsys and csv


Zunächst haben wir die ungeschwaerzt.pdf und ungeschwaerzt_markiert.pdf  zu Text Dateien umgewandelt, damit wir mit unterschiedlichen Programmiersprachen an der Textdatei arbeiten können.
Als nächstes haben wir versucht mit hilfe regular expression die Textdatei zu entschlacken, d.h. den Text zu cleanen und komprimiert darzustellen.

In dieser Datei haben wir dann nach Stellen gesucht die mit “X” geschwärzt wurden und haben anhand dessen einen geschwärzten Anteil von ca. 0,5% berechnet.
Diesen Wert fanden wir wenig Aussagekräftig und entschieden uns deshalb dazu den markierten Anteil im Text zu analysieren.
Dazu konvertierten wir jede Seite der Datei zu JPGs und suchten nach dem Gelbanteil mit imagesearch.
Bei der Auswertung von Seite 1587 kamen wir auf einen Markierten Anteil von ca. 9%.

Danach versuchten wir in der Datei nach Namen zu suchen
Dafür verglichen wir die Namen in der alleVornamen.txt Datei mit der ungeschwärzten Datei und filterten die Namen die miteinander übereinstimmten heraus.
Jedoch stießen wir auf das Problem, dass es auch mit Straßen-, Ortsnamen oder Monaten zu Übereinstimmungen kam.


 
