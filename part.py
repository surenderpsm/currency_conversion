import glob
import os

try:
    os.mkdir('images')
except OSError as error:
    print(error)

dirs = ['Rs.10','Rs.20','Rs.50','Rs.100', 'Rs.200','Rs.500','Rs.2000']

i=0
for dir in dirs:
    for image in glob.glob(os.path.join(dir, "*.jp*")):
        os.rename(image, os.path.join('images', image[len(dir)+1:]))