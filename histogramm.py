#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np
import json

json_data=open('PDFConverter\\data\\dict.json').read()

data = json.loads(json_data)
# (data)
arr = []
for e in data:
    arr.append(data[e])
print(arr)
x = np.random.normal(size = 1000)
plt.hist(arr, normed=True, bins=100)
plt.ylabel('Percentage')
plt.xlabel('100 pages with marked content')

plt.show()