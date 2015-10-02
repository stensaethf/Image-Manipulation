# chroma_key.py
# Takes an image and changes the background to a color or other image
# Created by Zoe Peterson and Frederik Roenn Stensaeth
# 02.05.14

# Import imaes library
from images import *


#Function to replace wall with color. Parameters are image that the user wants
#to change, and the RGB values of Red Green and Blue that the user wants 
#the background to be changed to. Returns image with new wall color.
def replaceWallWithColor(image, red, green, blue):
    
    
    #Get width and height of image
    width = image.getWidth()
    height = image.getHeight()
    
    #Loop over each pixel in image
    for i in range(width):
        for j in range(height):
            #Get color of pixel
            pixel_color = image.getPixel2D(i, j)
            #Call pixelColor function using parameters pixel_color, i, and j
            result = pixelColor(pixel_color, i, j)
            #If pixelColor function returns true execute if body
            if result == True:
                #Check to see if pixel near should also be changed
                if (i <= width) and (j <= (height - 2)):
                    #Get color of pixel located one down from (i, j) pixel 
                    pixel_color2 = image.getPixel2D(i, j + 1)
                    #Call pixelColor function using parameters pixel_color, i,
                    # and j + 1
                    result = pixelColor(pixel_color2, i, j)
                    #If pixelColor function returns true execute if body
                    if result == True:        
                        #Set pixel to color (red, green, blue) at position
                        #(i, j)
                        image.setPixel2D(i, j, (red, green, blue))
                else:
                    #If pixelColor function returned True for (i, j) but j + 1
                    #is out of range, still change pixel
                    image.setPixel2D(i, j, (red, green, blue))
    
    #Return image
    return image


#Function to determine if tuple at (i, j) is wall. 
#Parameters are i, j, and tuple at (i, j). 
#Returns True if color should be changed and False if not.
def pixelColor(tuple, i, j):
    
    
    #Store tuple as pixel_color
    pixel_color = tuple
    
    #If statement to determine if difference between red and green 
    #in pixel_color is less than or equal to 25
    if abs(pixel_color[0] - pixel_color[1]) <= 25:
        #If statement to determine if difference between red and blue 
        #in pixel_color is less than or equal to 25
        if abs(pixel_color[0] - pixel_color[2]) <= 25:
            #If statement to determine if difference between green and blue 
            #in pixel_color is less than or equal to 25
            if abs(pixel_color[1] - pixel_color[2]) <= 25:
                #If statement to determine if red and green in 
                #pixel_color are greater than or equal to 97
                if (pixel_color[0] >= 97) and (pixel_color[1] >= 97):
                    #Return True
                    return True
    else:
        #If one of the if statements is not met, return False
        return False
    

#Function to replace wall with image.
#Parameters are originalImage (image with person) and replacementImage 
#(new background). Returns image with new background.
def replaceWallWithImage(originalImage, replacementImage):
    
    
    #Call replaceWallWithColor function and change wall to rbg (0, 255, 0)
    #(green)
    image = replaceWallWithColor(originalImage, 0, 255, 0)
    
    #Get width and height of image
    width = image.getWidth()
    height = image.getHeight()
    
    #Loop over each pixel in image
    for i in range(width):
        for j in range(height):
            #Get color tuple for pixel (i, j)
            color = image.getPixel2D(i, j)
            #Execute if body if pixel (i, j) has rgb tuple (0, 255, 0)
            if (color[0] == 0) and (color[1] == 255) and (color[2] == 0):
                #Get tuple for pixel (i, j) in replacementImage
                backgr = replacementImage.getPixel2D(i, j)
                #Set pixel (i, j) in image to rgb tuple of pixel (i, j) 
                #in replacementImage
                image.setPixel2D(i, j, (backgr[0], backgr[1], backgr[2]))
     
    #Return image 
    return image
    

#Call upon other functions to change background (wall) of picture with person
#to desired color or other image. No parameters    
def main():
    
    
    #Ask user for image that wants new background
    image = raw_input('In which image do you want to a new background? ')
    
    # Make image object from image file
    image_original = FileImage(image)
    # Make copy
    copy = image_original.copy()
    
    #Ask user if they want a color or image background
    print 'Enter color for color background or image for'
    choice = raw_input('image background: ')
    
    #Execute if body if user wants color background
    if (choice == 'color') or (choice == 'Color'):
        #Ask user for rgb tuple to be user for background
        red = int(raw_input('Enter desired RGB value for red: '))
        green = int(raw_input('Enter desired RGB value for green: '))
        blue = int(raw_input('Enter desired RGB value for blue: '))
        #Call replaceWallWithColor function. Parameters are copy and desired
        #background color
        new_image = replaceWallWithColor(copy, red, green, blue)
        #Show image with color background
        new_image.show('Single Colored Background', 10, 10)
    
    #Execute elif body if user wants image background
    elif (choice == 'Image') or (choice == 'image'):
        #Ask user for image to be background
        background = raw_input('Which image do you want as background? ') 
        # Make image object from image file
        image_background = FileImage(background)
        # Make copy
        background_copy = image_background.copy()
        #Call replaceWallWithImage function. Parameters are copy and
        #background_copy
        new_image2 = replaceWallWithImage(copy, background_copy)
        #Show image with image background
        new_image2.show('Image with Image Background', 10, 10)
    
    #Wait for user to admire picture before closing
    raw_input('Enter to close')
    

if __name__ == '__main__':
    main()