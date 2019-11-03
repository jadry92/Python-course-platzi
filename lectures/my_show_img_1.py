#!/home/sebastian/anaconda3/bin/python

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import struct

def read_image_from_png(File_name):
    img = mpimg.imread(File_name)
    plt.figure()
    plt.imshow(img,cmap='jet')
    plt.draw()
    return img

def imag2vect(img,check):
    img_size = img.shape
    img_out = img.reshape([img_size[0]*img_size[1]*img_size[2],1],order='F')
    if check == True:
        for ix in range(0,img_size[0]):
            for iy in range(0,img_size[1]):
                for px in range(0,img_size[2]):
                    if img_out[0][ix + iy*img_size[0] + px*img_size[0]*img_size[1]] != img[ix][iy][px]:
                        print(img_out[0][ix + iy*img_size[0] + px*img_size[0]*img_size[1]],'=',img[ix][iy][px])
    
    return img_out

def save_img_in_bin(img_out,File_name):
    print(len(img_out))
    s = struct.pack('i'*len(img_out),*img_out)
    File_name_out = File_name + '.bin'
    print(File_name)
    f = open(File_name_out, "wb")
    f.write(s)
    f.close()
    

img = read_image_from_png('img_1.jpg')
img_out = imag2vect(img,False)
del img
save_img_in_bin(img_out,'image')

plt.show()