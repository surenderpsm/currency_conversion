import os
import random
import glob

img_train_path = 'images\\train'
img_val_path = 'images\\validation'

lab_train_path = 'labels\\train'
lab_val_path = 'labels\\validation'

try:
    os.mkdir(img_train_path)
    os.mkdir(img_val_path)
    os.mkdir(lab_train_path)
    os.mkdir(lab_val_path)
except OSError as error:
    print(error)

random.seed(10)

# edit here
train_ratio = 0.7
val_ratio = 1-train_ratio

images = glob.glob("images\*.jpg")

train_length = int(train_ratio*len(images))
test_length = len(images) - train_length

print("Allocating "+str(train_length)+" for training.")
print("Allocating "+str(test_length)+" for testing")

train = random.sample(images, k=train_length)
test = [image for image in images if image not in train]

print("Train and test sets created")

for item in train:
    item_name = item[len("images\\"):-4]
    os.rename(os.path.join("labels", item_name+".txt"), os.path.join(lab_train_path, item_name+".txt"))
    os.rename(os.path.join("images", item_name+".jpg"), os.path.join(img_train_path, item_name+".jpg"))
print("Prepared train directory")
for item in test:
    item_name = item[len("images\\"):-4]
    os.rename(os.path.join("labels", item_name+".txt"), os.path.join(lab_val_path, item_name+".txt"))
    os.rename(os.path.join("images", item_name+".jpg"), os.path.join(img_val_path, item_name+".jpg"))
print("Prepared validation directory")