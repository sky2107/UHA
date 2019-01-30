# UHA

Urban Hacking
Informatik Projekt

Felix Navas 1412100 <br>
Jonas Lagaude 1430596 <br>
Ahmed Warsame 1611148 <br>

requirements for this code base 
python 2.7 
libaries => PyPDF2, os, re, platform, PIL, colorsys, turtle, json and csv

- List of marked pages = [26, 27, 28, 30, 1323, 1324, 1328, 1336, 1337, 1373, 1375, 1376,1377, 1378, 1379, 1381, 1382, 1397, 1398, 1399, 1400, 1401,                            1402, 1403, 1404, 1405, 1406, 1407, 1408, 1409, 1410, 1411, 1412, 1413, 1414, 1415, 1416, 1417, 1418, 1419, 1420, 1422, 1424, 1425, 1427, 1428, 1429, 1430, 1431, 1432, 1433, 1434, 1435, 1444, 1445, 1457, 1460, 1473, 1477, 1481, 1484, 1486, 1487, 1488, 1489, 1490, 1491, 1493, 1495, 1497, 1498, 1499, 1500, 1501, 1506, 1507, 1509, 1511, 1512, 1513, 1514, 1531, 1532, 1534, 1535, 1536, 1537, 1539, 1557, 1558, 1561, 1562, 1563, 1565, 1567, 1572, 1577, 1578, 1587, 1601]

- How many pages are marked 100.
- Total of 1822 pages

![Histogramm](histogramm.PNG?raw=true)

Zunächst haben wir die ungeschwaerzt.pdf und ungeschwaerzt_markiert.pdf  zu Text Dateien umgewandelt, damit wir mit unterschiedlichen Programmiersprachen an der Textdatei arbeiten können.
Als nächstes haben wir versucht mit hilfe regular expression die Textdatei zu entschlacken, d.h. den Text zu cleanen und komprimiert darzustellen.

In dieser Datei haben wir dann nach Stellen gesucht die mit “X” geschwärzt wurden und haben anhand dessen einen geschwärzten Anteil von ca. 0,5% berechnet.
Diesen Wert fanden wir wenig Aussagekräftig und entschieden uns deshalb dazu den markierten Anteil im Text zu analysieren.
Dazu konvertierten wir jede Seite der Datei zu JPGs und suchten nach dem Gelbanteil mit imagesearch.
Bei der Auswertung von Seite 1587 kamen wir auf einen Markierten Anteil von ca. 9%.

Danach versuchten wir in der Datei nach Namen zu suchen
Dafür verglichen wir die Namen in der alleVornamen.txt Datei mit der ungeschwärzten Datei und filterten die Namen die miteinander übereinstimmten heraus.
Jedoch stießen wir auf das Problem, dass es auch mit Straßen-, Ortsnamen oder Monaten zu Übereinstimmungen kam.


 
