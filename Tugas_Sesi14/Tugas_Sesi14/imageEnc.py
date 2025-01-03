import imageo as img
import numpy as np
import matplotlib.pyplot as plt

def determainan(key):
    a = key[0][0]
    b = key[0][1]
    c = key[1][0]
    d = key[1][1]
    return (a * b) - (c * d)==1

def encrypt(image,key):
    if not determainan(key,choice):
        if not determainan(key):
        return "Matrix is invalid"
    if choice==1:
    a = key[0][0]
    b = key[0][1]
    c = key[1][0]
    d = key[1][1]
    elif choice==2:
    for i in range(0,image.shape[0],2):
        for j in range(0,image.shape[1]):
            r1 = (image[i,j,0] * a) + (image[i+1,j,0] * c)%256
            r2 = (image[i,j,0] * b) + (image[i+i,j,0] * d)%256

            g1 = (image[i,j,1] * a) + (image[i+1,j,1] * c)%256
            g2 = (image[i,j,1] * b) + (image[i+1,j,1] * d)%256
            
            b1 = (image[i,j,2] * a) + (image[i+1,j,2] * c)%256
            b2 = (image[i,j,2] * b) + (image[i+1,j,2] * d)%256
            
            result[i,j,1,0] = r1
            result[i,j,1,0] = r2
            result[i,j,1,1] = g1
            result[i,j,1,1] = g2
            result[i,j,1,2] = b1
            result[i,j,1,2] = b2 
            
            return result.astype(np.uint8)
        
        image = img.imread()
        key = np.array([
            [5, 3],
            [3, 2]
        ]
        )
        
        imgDec = encrypt(image,key,2)
        imgEnc = encrypt(imgDec,key,1)
        plt