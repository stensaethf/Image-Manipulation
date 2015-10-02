# photolab3.py
# Python module that either scales an image, blurs an image, or rotates an
# image to the left.
# Created by Frederik Roenn Stensaeth
# 02.08.14 (mm.dd.yy)

from images import *


def rotate_left(image):
    

    width = image.getWidth()
    height = image.getHeight()
    
    new_image = EmptyImage(height, width)

    for i in range(width):
        for j in range(height):
            color = image.getPixel2D(i, j)
            new_image.setPixel2D(height + 1 - j, width + 1 - i, color)

    return new_image


def blur(image, radius):

    
    red = 0
    green = 0
    blue = 0

    width = image.getWidth()
    height = image.getHeight()

    new_image = EmptyImage(width, height)

    for i in range(width):
        for j in range(height):

            count = 0

            if ((i - radius) >= 0) and ((i + radius) <= width):

                if ((j - radius) >= 0) and ((j + radius) <= height):

                    for a in range(i - radius, i + radius + 1):

                        for b in range(j - radius, j + radius + 1):

                            pixel = image.getPixel2D(a, b)
                            red += pixel[0]
                            green += pixel[1]
                            blue += pixel[2]
                            count += 1

                else:

                    if ((j + radius) > height):

                        for a in range(i - radius, i + radius + 1):

                            for b in range(j - radius, height + 1):

                                pixel = image.getPixel2D(a, b)
                                red += pixel[0]
                                green += pixel[1]
                                blue += pixel[2]
                                count += 1

                    else:

                        for a in range(i - radius, i + radius + 1):

                            for b in range(0, j + radius + 1):

                                pixel = image.getPixel2D(a, b)
                                red += pixel[0]
                                green += pixel[1]
                                blue += pixel[2]
                                count += 1

            elif:

                if ((i - radius) < 0):

                    if ((j - radius) < 0):

                        for a in range(0, i + radius + 1):

                            for b in range(0, j + radius + 1):

                                pixel = image.getPixel2D(a, b)
                                red += pixel[0]
                                green += pixel[1]
                                blue += pixel[2]
                                count += 1

                    elif ((j + radius) > height):

                        for a in range(0, i + radius + 1):

                            for b in range(j - radius, height + 1):

                                pixel = image.getPixel2D(a, b)
                                red += pixel[0]
                                green += pixel[1]
                                blue += pixel[2]
                                count += 1
                    else:

                        for a in range(0, i + radius + 1):

                            for b in range(j - radius, j + radius + 1):

                                pixel = image.getPixel2D(a, b)
                                red += pixel[0]
                                green += pixel[1]
                                blue += pixel[2]
                                count += 1

                else: # ((i + radius) > width)

                    if ((j - radius) < 0)):

                        for a in range(i - radius, width + 1):

                            for b in range(0, j + radius + 1):

                                pixel = image.getPixel2D(a, b)
                                red += pixel[0]
                                green += pixel[1]
                                blue += pixel[2]
                                count += 1

                    elif ((j + radius) > height):

                        for a in range(i - radius, width + 1):

                            for b in range(j - radius, height + 1):

                                pixel = image.getPixel2D(a, b)
                                red += pixel[0]
                                green += pixel[1]
                                blue += pixel[2]
                                count += 1

                    elif ((j - radius) >= 0) and ((j + radius) <= height):
                        
                        for a in range(i - radius, width + 1):

                            for b in range(j - radius, j + radius + 1):

                                pixel = image.getPixel2D(a, b)
                                red += pixel[0]
                                green += pixel[1]
                                blue += pixel[2]
                                count += 1
                                
            red = red / count
            green = green / count
            blue = blue / count
            confirm = new_image.getPixel2D(i, j) # NEEDED??
            if confirm == (255, 255, 255): # NEEDED??
                new_image.setPixel2D(i, j, (red, green, blue))

    return new_image


def scale(image, scaling):


    width = image.getWidth()
    height = image.getHeight()

    new_image = EmptyImage(width * scaling, height * scaling)

    new_width = new_image.getWidth()
    new_height = new_image.getHeight()

    pixel_count = float(1 / scaling)

    for i in range(new_width):
        for j in range(new_height):
            pixel_width = int(pixel_count * i)
            pixel_height = int(pixel_count * j)
            color = image.getPixel2D(pixel_width, pixel_height)
            new_image.setPixel2D(i, j, color)

    return new_image


def main():

    
    image = raw_input('Choose an image: ')
    
    choice = raw_input('Do you want to scale, blur, or rotate an image? ')

    if (choice == Scale) or (choice == scale):
        scaling = raw_input('Enter scaling factor: ')
        scaled_image = scale(image, scaling)
        scaled_image.show()

    elif (choice == Blur) or (choice == blur):
        radius = raw_input('Enter bluring radius: ')
        blured_image = blur(image, radius)
        blured_image.show()

    elif (choice == Rotate) or (choice == rotate):
        rotated_image = rotate_left(image)
        rotated_image.show()

    raw_input('Enter to close')


if __name__ == '__main__':
    main()