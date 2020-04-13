# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 19:47:08 2020

@author: AlbertYang
jasnei@163.com
version v1.0
"""


import PySimpleGUI as sg
import cv2
import numpy as np

"""
Demo program that displays image using OpenCV and applies some very basic image functions

- functions from top to bottom -
Gray:       change image color to Gray
HSV:        change image color to HSV
LUV:        change image color to LUV
LAB:        change image color to LAB
YUV:        change image color to YUV
Cal_EQ:     Image equalizeHist
threshold:  simple b/w-threshold on the luma channel, slider sets the threshold value
canny:      edge finding with canny, sliders set the two threshold values for the function => edge sensitivity
contour:    contour finding in the frame, slider sets the value of threshold for b/w using threshold to find
            Found objects are drawn with a red contour.
blur:       simple Gaussian blur, slider sets the sigma, i.e. the amount of blur smear

"""


def main():
    
    sg.theme('LightBlue')
    
    # Popup window get Image file
    filename = sg.popup_get_file('Please Input a Image')
    if filename is None:
        return
    
    # two image windows, image_orginal display orginal image, image_frame1 for processing
    image_layout = [
    [sg.Image(filename='', key='image_original'), sg.Image(filename='', key='image_frame1')]
    
    ]
    
    # define Radio & Sliders
    radio_layout = [
       
    # [sg.Radio('None', 'Radio', True, size=(10, 1))],
    [sg.Radio('Gray', 'Radio', size=(10, 1), key='Gray'),
     sg.Radio('HSV', 'Radio', size=(10, 1), key='HSV'), 
     sg.Radio('LUV', 'Radio', size=(10, 1), key='LUV'),
     sg.Radio('LAB', 'Radio', size=(10, 1), key='LAB'),
     sg.Radio('YUV', 'Radio', size=(10, 1), key='YUV'),
     sg.Radio('Cal_EQ', 'Radio', size=(10, 1), key='Cal_EQ')],
      
    [sg.Radio('Threshold', 'Radio', size=(10, 1), key='thresh'),
     sg.Slider((0, 255), 128, 1, orientation='h', size=(40, 15), key='thresh_slider')],
      
    [sg.Radio('Canny', 'Radio', size=(10, 1), key='canny'),
     sg.Text('Min', size=(3,1), justification = 'left'),
     sg.Slider((0, 255), 128, 1, orientation='h', size=(16, 15), key='canny_slider_a'),
     sg.Text('Max',size=(3,1), justification = 'left'),
     sg.Slider((0, 255), 128, 1, orientation='h', size=(16, 15), key='canny_slider_b')],
      
    [sg.Radio('Contour', 'Radio', size=(10, 1), key='contour'),
     sg.Slider((0, 255), 128, 1, orientation='h', size=(40, 15), key='contour_slider'),],
      
    [sg.Radio('Blur', 'Radio', size=(10, 1), key='blur'),
     sg.Slider((1, 11), 1, 1, orientation='h', size=(40, 15), key='blur_slider')], 
      
    [sg.Radio('enhance', 'Radio', size=(10, 1), key='enhance'),
     sg.Slider((1, 255), 128, 1, orientation='h', size=(40, 15), key='enhance_slider')],
              ]
    
    # define Layout for image & Functions, functions including radio & sliders
    layout = [
    
    [sg.Frame('Image', image_layout)],
    [sg.Frame('Function', radio_layout)], 
    [sg.Text('')],
    [sg.Button('Exit', size=(10, 1))],
    ]
    
    # define Window
    window = sg.Window('Learn OpenCV',
           layout,
           location=(450, 200),
           finalize=True)
    
    # define function to get Image using Opencv function, & resize according to avoid windows too big
    def get_image():
        img_src = cv2.imread(filename)
        rows, cols = img_src.shape[:2]
    
        if rows <= 300:
            img_resize = img_src.copy()
            img_copy = img_resize.copy()
        if rows > 300 and rows <= 512:
            img_resize = cv2.resize(img_src, None, fx = 0.8, fy =0.8)
            img_copy = img_resize.copy()
        if rows >512 and rows <=1080:
            img_resize = cv2.resize(img_src, None, fx = 0.6, fy =0.6)
            img_copy = img_resize.copy()   
        if rows >1080:
            img_resize = cv2.resize(img_src, None, fx = 0.3, fy =0.3)
            img_copy = img_resize.copy()
        if rows >2000:
            img_resize = cv2.resize(img_src, None, fx = 0.2, fy =0.2)
            img_copy = img_resize.copy()
        return img_resize, img_copy
        
    
    
    frame, frame1 = get_image()
    
    # putText 'Oringinal Image on the frame.
    frame = cv2.putText(frame, 'Original Image', (10,25), cv2.FONT_HERSHEY_COMPLEX, 0.5, (165,255,255),2)
    
    # here define all the functions
    while True:
        event, values = window.read(timeout=0, timeout_key='timeout')
        if event == 'Exit' or event is None:
            break
        
        if values['Gray']:
            frame1 = get_image()[1]
            frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
          
        if values['HSV']:
            frame1 = get_image()[1]
            frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)
           
        if values['LUV']:
            frame1 = get_image()[1]
            frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2LUV)
            
        if values['LAB']:
            frame1 = get_image()[1]
            frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2LAB)
        
        if values['YUV']:
            frame1 = get_image()[1]
            frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2YUV)
        
        if values['LAB']:
            frame1 = get_image()[1]
            frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2LAB)
        
        if values['Cal_EQ']:
            frame1 = get_image()[1]
            (b, g, r) = cv2.split(frame1)
            bH = cv2.equalizeHist(b)
            gH = cv2.equalizeHist(g)
            rH = cv2.equalizeHist(r)
            # merge R G B channel
            frame1 = cv2.merge((bH, gH, rH))
                      
        if values['thresh']:
            frame1 = get_image()[1]
            frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
            frame1 = cv2.threshold(frame1, values['thresh_slider'], 255, cv2.THRESH_BINARY)[1]
        
        if values['canny']:
            frame1 = get_image()[1]
            # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame1 = cv2.Canny(frame1, values['canny_slider_a'], values['canny_slider_b'])
        
        if values['blur']:
            frame1 = get_image()[1]
            frame1 = cv2.GaussianBlur(frame1, (21, 21), values['blur_slider']) 
        
        if values['contour']:
            frame1 = get_image()[1]
            imgray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
            ret, thresh = cv2.threshold(imgray,values['contour_slider'], 255, cv2.THRESH_BINARY)
            contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            cv2.drawContours(frame1, contours, -1, (0, 0, 255), 2)
            
        if values['enhance']:
            frame1 = get_image()[1]
            enh_val = values['enhance_slider'] / 40
            clahe = cv2.createCLAHE(clipLimit=enh_val, tileGridSize=(8, 8))
            lab = cv2.cvtColor(frame1, cv2.COLOR_BGR2LAB)
            lab[:, :, 0] = clahe.apply(lab[:, :, 0])
            frame1 = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
           
        imgbytes = cv2.imencode('.png', frame)[1].tobytes()
        window['image_original'].update(data=imgbytes)
        imgbytes = cv2.imencode('.png', frame1)[1].tobytes()
        window['image_frame1'].update(data=imgbytes)
    
    window.close()


main()
