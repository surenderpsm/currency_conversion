import glob
import os

path = 'unannotated'

try:
    os.mkdir(path)
except OSError as error:
    print(error)
    
i=0
for img in glob.glob("images\*.jpg"):
    img_name = img[len("images\\"):-4]
    if "labels\\"+img_name+".txt" not in glob.glob("labels\*.txt"):
        print("labels\\"+img_name+".txt"+"\t"+str(i))
        i+=1
        os.rename(img, os.path.join(path, img_name+".jpg"))