'''program with functions that edits a folder with images(png format)'''
from hmcpng import *

def create_uniform_image(height, width, pixel):
    """ creates and returns a 2-D list of pixels with height rows and
        width columns in which all of the pixels have the RGB values
        given by pixel
        inputs: height and width are non-negative integers
                pixel is a 1-D list of RBG values of the form [R,G,B],
                     where each element is an integer between 0 and 255.
    """
    pixels = []

    for r in range(height):
        row = [pixel] * width
        pixels += [row]

    return pixels

def blank_image(height, width):
    """ creates and returns a 2-D list of pixels with height rows and
        width columns in which all of the pixels are green.
        inputs: height and width are non-negative integers
    """
    all_green = create_uniform_image(height, width, [0, 255, 0])
    
    return all_green

def brightness(pixel):
    """ takes a pixel (an [R, G, B] list) and returns a value
        between 0 and 255 that represents the brightness of that pixel.
    """
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]
    
    return (21*red + 72*green + 7*blue) // 100

## put your functions below

# problem 1

def bw(pixels, threshold):
    """ turns given image into black and white """
    
    black = [0, 0, 0]
    white = [255, 255, 255]
    height = len(pixels)  
    width = len(pixels[0])
    new_pixels = blank_image(height, width)
    
    for r in range(height):
        for c in range(width):
            
            if brightness(pixels [r] [c]) > threshold :
                new_pixels [r] [c] = white
                
            elif brightness(pixels [r] [c]) <= threshold :
                new_pixels [r] [c] = black
                
    return new_pixels

# problem 2 
def fold_diag(pixels):
    """ takes given image and folds is diagonally """
    
    height = len(pixels) 
    width = len(pixels[0])
    white = [255, 255, 255]
    new_pixels = create_uniform_image(height, width,  [0, 255, 0] )
    white = [255, 255, 255]
    
    for r in range(height):
        for c in range(width):
            if  [r] > [c]:
                
                new_pixels[r] [c] = white
            elif [r] <= [c]:
                
                new_pixels[r] [c] = pixels [r] [c]
                
    return new_pixels

# problem 3
def  mirror_horiz(pixels):
    """ takes given image and mirrors it from the middle vertically """
    
    height = len(pixels)  
    width = len(pixels[0])
    new_pixels = create_uniform_image(height, width,  [0, 255, 0] )
    
    for r in range(height):
        for c in range(width):
            holder = c
            if [c] >= [len(pixels[0]) // 2]:
                
                new_pixels [r] [c] = pixels [r] [c - (1 + holder +c)]
            elif [c] <= [len(pixels[0]) // 2]:
                new_pixels [r] [c] = pixels [r] [c]

    return new_pixels

# problem 4
def extract(pixels, rmin, rmax, cmin, cmax):
    """ cuts a certain part of an image and copies it """
    
    rdiff = (rmax - rmin)
    cdiff = (cmax - cmin)
    new_image = create_uniform_image((rdiff), (cdiff),  [0, 255, 0] )
    
    for r in range(rdiff):
        for c in range(cdiff):
            
            if r >= rmin or r < rmax  and c  >= cmin or c < cmax :
                
                new_image [r] [c] = pixels [r + rmin] [c + cmin]
                
    return new_image

# problem 5
def transpose(pixels):
    """ flips the image on its side """
    
    height = len(pixels)
    width = len(pixels[0])
    new_pixels = create_uniform_image(width, height,  [0, 255, 0] )
    
    for r in range(width):
        for c in range(height):
            
            new_pixels[r][c] = pixels[c][r] 
            
           
            
    return new_pixels
