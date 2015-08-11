#! /usr/bin/python

'''
Gaussian smoothing with Python.
'''

import cv2
import numpy as np
import math
from scipy.signal import sepfir2d

def gaussian_filter(sigma, filter_length=None):
    '''
    Given a sigma, return a 1-D Gaussian filter.
    @param     sigma:         float, defining the width of the filter
    @param     filter_length: optional, the length of the filter, has to be odd
    @return    A 1-D numpy array of odd length, 
               containing the symmetric, discrete approximation of a Gaussian with sigma
               Summation of the array-values must be equal to one.
    '''
    if filter_length==None:
        #determine the length of the filter
        filter_length= math.ceil(sigma*5) 
        #make the length odd
        filter_length= 2*(int(filter_length)/2) +1   
    
    #make sure sigma is a float
    sigma=float(sigma)
    
    #create the filter
    result = np.arange( filter_length , dtype=np.float64)
    result = np.subtract(result, filter_length/2)
    result = np.divide(result, sigma)
    result = np.square(result)
    result = np.multiply(result, -0.5)
    result = np.exp(result)
    result = np.divide(result, 2.0)
    #return the filter
    return result


def test_gaussian_filter():
    '''
    Test the Gaussian filter on a known input.
    '''
    sigma = math.sqrt(1.0/2/math.log(2))
    f = gaussian_filter(sigma, filter_length=3)
    correct_f = np.array([0.25, 0.5, 0.25])
    error = np.abs( f - correct_f)
    if np.sum(error)<0.001:
        print "Congratulations, the filter works!"
        cv2.waitKey(0)

    else:
        print "Still some work to do.."
        
      

    
def gaussian_smooth1(img, sigma): 
    '''
    Do gaussian smoothing with sigma.
    Returns the smoothed image.
    '''
    result = np.zeros_like(img, dtype=np.float64)
    
    #get the filtercv2.waitKey(0)
    filter = gaussian_filter(sigma)
    
    #smooth every color-channel
    for c in range(3):
        #smooth the 2D image img[:,:,c]
        #tip: make use of numpy.convolve
        
        #apply numpy.convolve for rows and
        #then for the columns
        result[:,:,c] = sepfir2d(img[:,:,c], filter, filter)
           
    
    return result



#this part of the code is only executed if the file is run stand-alone
if __name__ == '__main__':
    #test the gaussian filter
    test_gaussian_filter()

    #read an image
    img = cv2.imread('face.tiff').astype(np.float64)
    
    #print the dimension of the image
    print img.shape
    
    #show the image, and wait for a key to be pressed
    cv2.imshow('img',img)
    cv2.waitKey(0)
    
    #smooth the image
    smoothed_img = gaussian_smooth1(img, 2)
    
    #show the smoothed image, and wait for a key to be pressed
    cv2.imshow('smoothed_img',smoothed_img)
    cv2.waitKey(0)
    
