from typing import Literal
from PIL import Image, ImageDraw, ImageFont
import os, glob
import numpy as np
import random
import cv2
from boudning_box_c import get_bounding_box_character
from pre_process import pre_process_characer
WIDTH = 64
HEIGTH = 64

#Create paths to attach dataset
if not os.path.exists('../datasets/ocr'):
    os.mkdir('../datasets/ocr')

    os.mkdir('../datasets/ocr/labels')
    os.mkdir('../datasets/ocr/images')


#define destination paths
img_dst_path = '../datasets/ocr/images'
label_dst_path = '../datasets/ocr/labels'
charactersList=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                'A','B','D','E','F','G','H','I','J','K','L','M','N','O','Q','R','T','Y',
                '0','1','2','3','4','5','6','7','8','9',
                '.',',','[',']','(',')','-',':',';','{','}','?','#','%','&','=','"','!','*','@']
                # 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
#83 characters
fontTypes=[]
print(len(charactersList))

for font in glob.glob("fonts/*"): # Create Image for every font
    
    fontTypes.append(os.path.abspath(font))
    
    print(len(fontTypes), font)



for count, character in enumerate(charactersList):
    
    for font in fontTypes:
        #extract, center and draw letter&font to image.
        # save to dataset/images/___.png
            font_name =str(font).split('.')
            font_name=font_name[0].split('/')
            dst_name_img    = os.path.join(img_dst_path, font_name[-1])
            dst_name_label  = os.path.join(label_dst_path, font_name[-1])

            img = Image.new("L", (WIDTH, HEIGTH), color=(255)) 
           

            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype(font, 48)
            w, h = draw.textsize(character, font=font)
            draw.text(((WIDTH-w)/2, (HEIGTH-h)/2), text=character, fill='black', font=font)

            # img2 = Image.new("L", (WIDTH, HEIGTH), color=(255)) 

            # draw2 = ImageDraw.Draw(img2)
            
            # w, h = draw2.textsize(character, font=font)
            # draw2.text(((WIDTH-w)/2, (HEIGTH-h)/2), text=character, fill='black', font=font)
       


        #calculate bounding box of character.
        #write coordinates to txt files dataset/labels/___.txt
            # size_width, size_height = draw.textsize(character, font)

            processed_img = pre_process_characer(img)
            rect = get_bounding_box_character(processed_img)
           
            #if bounding box was not possible to obtain, exclude the image
            if len(rect)!=4:
                print(f'failed to obtain bounding box for {dst_name_img}_{character}')
                continue
            #center by the dynamic position from max/min coordinates in histogram analysis
            x_center=   ((rect[2]+rect[0])/2)/WIDTH
            y_center=  ((rect[3]+rect[1])/2)/HEIGTH
            
            #convert to  width_heigth YOLO format
            w_=  (rect[2]-rect[0])/WIDTH
            h_=  (rect[3]-rect[1])/HEIGTH

            # f.write(f"{count} {x_center} {y_center} {w_} {h_}")
            # f.close()
            # x1 = 32-size_width/2
            # y1 = 32-size_height/2
            # x2 = 32+size_width/2
            # y2 = 32+size_height/2


            # draw2.rectangle([(rect[1], rect[0]), (rect[3], rect[2])],width=1)
            # draw2.rectangle(rect,width=1)

            # img2.save(character+'.png')
            

            f= open(f"{dst_name_label}_{character}.txt","w+")
            f.write(f"{count} {x_center} {y_center} {w_} {h_}")
            cv2.imwrite(f'{dst_name_img}_{character}.png', processed_img)
            f.close()
            # input()


            # input()
    print(count,'/',len(charactersList)-1)
            
            