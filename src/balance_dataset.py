import sys
from genericpath import exists
import os
import random
import pathlib
import shutil
img_src = '../datasets/ocr/images'
label_src = '../datasets/ocr/labels'

train_ratio  = 70
val_ratio   =27
test_ratio  =3

count_img = 0
count_lbl = 0
for path in pathlib.Path(img_src).iterdir():
    if path.is_file():
        count_img += 1
print('images: ',count_img)

for path in pathlib.Path(label_src).iterdir():
    if path.is_file():
        count_lbl += 1
print('labels: ',count_lbl)



train_ratio_num  = int(count_img*0.70)
val_ratio_num   = int(count_img*0.27)
test_ratio_num   = int(count_img*0.03)



print(train_ratio_num)
print(val_ratio_num)
print(test_ratio_num)

print(train_ratio_num+val_ratio_num+test_ratio_num)

retval = input('is OK? y/n\n')
if retval != 'y':
    sys.exit()


img_files = os.listdir(img_src)

if not os.path.exists('../datasets/ocr/train'):
    os.mkdir('../datasets/ocr/train')
    os.mkdir('../datasets/ocr/val')
    os.mkdir('../datasets/ocr/test')

    os.mkdir('../datasets/ocr/train/labels')
    os.mkdir('../datasets/ocr/train/images')
    os.mkdir('../datasets/ocr/val/labels')
    os.mkdir('../datasets/ocr/val/images')
    os.mkdir('../datasets/ocr/test/labels')
    os.mkdir('../datasets/ocr/test/images')






for file in random.sample(img_files, train_ratio_num):
    try:
        img_path =os.path.join(img_src, file)
        file1 = file.split('.')
        if len(file1)>2:
            # if file1[2][0]=='.':
                file1[0] =file1[0]+'.'

        file1 = file1[0]+'.txt'
        if file1[0]=="'":
            file1 = file1[1:]
        
       
        
        label_path = os.path.join(label_src, file1)
        if os.path.exists(img_path) and os.path.exists(label_path):
            shutil.move(img_path,   '../datasets/ocr/train/images')
            shutil.move(label_path, '../datasets/ocr/train/labels')
        
    except:
        print('error at train set', file, file1)
        input()
    print(file1,'\r')


img_files2 = os.listdir(img_src)

for file in random.sample(img_files2, val_ratio_num):
    try:
        img_path =os.path.join(img_src, file)
        file1 = file.split('.')
        if len(file1)>2:
            # if file1[2][0]=='.':
                file1[0] =file1[0]+'.'

        file1 = file1[0]+'.txt'
        if file1[0]=="'":
            file1 = file1[1:]
        
       
        
        label_path = os.path.join(label_src, file1)
        if os.path.exists(img_path) and os.path.exists(label_path):
            shutil.move(img_path,   '../datasets/ocr/val/images')
            shutil.move(label_path, '../datasets/ocr/val/labels')
        
    except:
        print('error at val set', file, file1)
        input()
    print(file1,'\r')

img_files3 = os.listdir(img_src)

for file in img_files3:
    try:
        img_path =os.path.join(img_src, file)
        file1 = file.split('.')
        if len(file1)>2:
            # if file1[2][0]=='.':
                file1[0] =file1[0]+'.'

        file1 = file1[0]+'.txt'
        if file1[0]=="'":
            file1 = file1[1:]
        
       
        
        label_path = os.path.join(label_src, file1)
        if os.path.exists(img_path) and os.path.exists(label_path):
            shutil.move(img_path,   '../datasets/ocr/test/images')
            shutil.move(label_path, '../datasets/ocr/test/labels')
        
    except:
        print('error at test set', file, file1)
        input()
    print(file1,'\r')