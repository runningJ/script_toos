#coding:utf-8
#########################################################################
# File Name: data_augmentor.py
# Author:Lei Jiang
# mail: jianglei@1000look.com
# Created Time: 2016年04月12日 星期二 15时42分46秒
# Copyright Nanjing Qing So information technology
#########################################################################

from skimage import color
from skimage import io
from PIL import Image
from PIL import ImageEnhance
import numpy as np
import matplotlib.pyplot as plt

class Data_augmentor(object):
    def __init__(self):
        pass

    def change_brightness(self,img_path,factor):
        '''change image brightness factor:0.0:black,1.0:original'''
        img=Image.open(img_path)
        img=img.convert('RGB')
        img_enhance=ImageEnhance.Brightness(img)
        res=img_enhance.enhance(factor)
        method_name='bright'
        return res,method_name

    def change_contrast(self,img_path,factor):
        '''change image contrast factor:0.0:solid grey image,1.0:original'''
        img=Image.open(img_path)
        img=img.convert('RGB')
        img_enhance=ImageEnhance.Contrast(img)
        res=img_enhance.enhance(factor)
        method_name='contrast'
        return res,method_name

    def change_sharpness(self,img_path,factor):
        '''change image sharpness factor:0.0 blured image,2.0 sharped image,1.0
        original'''
        img=Image.open(img_path)
        img=img.convert('RGB')
        img_enhance=ImageEnhance.Sharpness(img)
        res=img_enhance.enhance(factor)
        method_name='sharpness'
        return res,method_name

    def rotate_image(self,img_path,angle):
        img=Image.open(img_path)
        res=img.rotate(angle,Image.NEAREST,expand=1)
        method_name='rotate'
        return res,method_name

    def change_color(self,img_path,factor):
        '''change image color factor:0.0 black and white 1.0 original'''
        img=Image.open(img_path)
        img=img.convert('RGB')
        img_enhance=ImageEnhance.Color(img)
        res=img_enhance.enhance(factor)
        method_name='color'
        return res,method_name
        


if __name__=="__main__":
    plt.subplot(121)
    ori=plt.imread('/opt/jl/datasets/car_plate/train/images/160.jpg')
    plt.imshow(ori)
##############################################
    da=Data_augmentor()
    res,_=da.change_brightness('/opt/jl/datasets/car_plate/train/images/160.jpg',0.5)
    res=np.array(res)
    plt.subplot(122)
    plt.imshow(res) 
    plt.show()
