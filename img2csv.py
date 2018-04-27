from __future__ import division
import numpy as np
import cv2
import collections
import sys
import os

# PATH = '/Users/truongnm/Downloads/data/images/04015.png'
PATH = sys.argv[1]
filename = os.path.splitext(os.path.basename(PATH))[0]
img = cv2.imread(PATH)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


indices = np.where(img == [68]) # where pixel is pink (pink -> gray = 68)
coordinates = np.array(list(zip(indices[1], indices[0])))  # -> coordinates[x, y]
coordinates = coordinates[coordinates[:,0].argsort()] # sort and calculate mean value of identical items
values_by_key = collections.defaultdict(list)
for k, v in coordinates:
    values_by_key[k].append(v)
coordinates = sorted([(k, sum(v) / len(v)) for k, v in values_by_key.items()])

with open('img2csv/%s-converted.csv' % filename, 'w+') as f:
    for index, coordinate in enumerate(coordinates):        
        f.write('{0},{1}\n'.format((coordinate[0]-56)*0.004, round((122 - coordinate[1])/70, 3)))
