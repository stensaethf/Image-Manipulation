# photolab3.py
# Python module that either scales an image, blurs an image, or rotates an
# image to the left.
# Created by Frederik Roenn Stensaeth
# 02.08.14 (mm.dd.yy)

# Import images library
from images import *


# Define rotate_left() function. Rotate_left() function rotates a given image
# to the left and returns the rotated image. Parameter is image. 
def rotate_left(image):
    
    
    # Get width and height of image
    width = image.getWidth()
    height = image.getHeight()
    
    # Create empty image with opposite height and width of image 
    new_image = EmptyImage(height, width)

    # For loop to loop over width and height
    for i in range(width):
        for j in range(height):
        
            # Get color tuple of pixel (i, j)
            pixel = image.getPixel2D(i, j)
            
            # Set color tuple to corresponding pixel in empty image 
            new_image.setPixel2D(j, i, pixel)

    # Return new_image
    return new_image


# Define blur() function. Blur() function averages out the red, green, and
# blue values of pixels within a certain radius of any given pixel, and
# creates and returns a new image with those averaged tuples. Parameters are
# image and radius.
def blur(image, radius):

    
    # Set red, green, and blue to be 0
    red = 0
    green = 0
    blue = 0

    # Get width and height of image
    width = image.getWidth()
    height = image.getHeight()

    # Create empty image of same width and height as image
    new_image = EmptyImage(width, height)
    
    # If statement to check whether radius is smaller than 0
    if radius < 0:
        # Return error message
        return 'Invalid radius entered.'
    
    # Elif statement to check if scaled image should be same size as original
    # image
    elif radius == 0:
    
        # Return original image
        return image
    
    # Else statement to be executed if radius is > 0
    else:
    
        # Foor loop to loop over width and height
        for i in range(width):
            for j in range(height):

                # Set count to be 0
                count = 0

                # If statement to check if (i ± radius) is within the limits
                # of the frame
                if ((i - radius) >= 0) and ((i + radius) <= width):

                    # If statement to check if (j ± radius) is within the
                    # limits of the frame
                    if ((j - radius) >= 0) and ((j + radius) <= height):

                        # For loop to loop over pixel (i, j) ± radius in both
                        # directions
                        for a in range(i - radius, i + radius):
                            for b in range(j - radius, j + radius):

                                # Get color tuple of pixel (a, b)
                                pixel = image.getPixel2D(a, b)
                                
                                # Accumulate the red, green, and blue values
                                red += pixel[0]
                                green += pixel[1]
                                blue += pixel[2]
                                
                                # Accumulate count variable
                                count += 1

                    # Else statement body to be executed if (j ± radius) is
                    # outside limits of the frame
                    else:
                        
                        # If statement to check if (j + radius) is larger than
                        # height
                        if ((j + radius) > height):

                            # For loop to loop over pixel (i, j) ± radius
                            # horizontally 
                            for a in range(i - radius, i + radius):
                                # For loop to loop over (j - radius) to height
                                for b in range(j - radius, height):

                                    # Get color tuple of pixel (a, b)
                                    pixel = image.getPixel2D(a, b)
                                    
                                    # Accumulate the red, green, and blue 
                                    # values
                                    red += pixel[0]
                                    green += pixel[1]
                                    blue += pixel[2]
                                    
                                    # Accumulate count variable
                                    count += 1

                        # Else statement body to be executed if (j + radius) is
                        # smaller than or equal to height
                        else:

                            # For loop to loop over (i ± radius)
                            for a in range(i - radius, i + radius):

                                # For loop to loop over 0 to (j + radius)
                                for b in range(0, j + radius):

                                    # Get color tuple of pixel (a, b)
                                    pixel = image.getPixel2D(a, b)
                                    
                                    # Accumulate the red, green, and blue
                                    # values
                                    red += pixel[0]
                                    green += pixel[1]
                                    blue += pixel[2]
                                    
                                    # Accumulate count variable
                                    count += 1

                # Else statement body to be executed if i ± radius is outside
                # of the limits of the frame
                else:

                    # If statement to check if (i - radius) is less than 0
                    if ((i - radius) < 0):

                        # If statement to check if (j - radius) is less than 0
                        if ((j - radius) < 0):

                            # For loop to loop over 0 to (i + radius)
                            for a in range(0, i + radius):

                                # For loop to loop over 0 to (j + radius)
                                for b in range(0, j + radius):

                                    # Get color tuple of pixel (a, b)
                                    pixel = image.getPixel2D(a, b)
                                    
                                    # Accumulate the red, green, and blue
                                    # values
                                    red += pixel[0]
                                    green += pixel[1]
                                    blue += pixel[2]
                                    
                                    # Accumulate count varible
                                    count += 1

                        # Elif statement to check if (j + radius) is larger
                        # than height
                        elif ((j + radius) > height):

                            # For loop to loop over 0 to (i + radius)
                            for a in range(0, i + radius):

                                # For loop to loop over (j - radius) to height
                                for b in range(j - radius, height):
                            
                                    # Get color tuple of pixel (a, b)
                                    pixel = image.getPixel2D(a, b)
                                    
                                    # Accumulate the red, green, and blue
                                    # values
                                    red += pixel[0]
                                    green += pixel[1]
                                    blue += pixel[2]
                                    
                                    # Accumulate count variable
                                    count += 1
                        
                        # Else statement to be executed if (j ± radius) is
                        # within the limits of the frame vertically
                        else:

                            # For loop to loop over 0 to (i + radius)
                            for a in range(0, i + radius):

                                # For loop to loop over (j ± radius)
                                for b in range(j - radius, j + radius):

                                    # Get color tuple of pixel (a, b)
                                    pixel = image.getPixel2D(a, b)
                                    
                                    # Accumulate the red, green, and blue
                                    # values
                                    red += pixel[0]
                                    green += pixel[1]
                                    blue += pixel[2]
                                    
                                    # Accumulate count variable
                                    count += 1

                    # Else statement to be executed if (i + radius) is larger
                    # than width
                    else:

                        # If statement to check if (j - radius) is less than 0
                        if ((j - radius) < 0):

                            # For loop to loop over (i - radius) to width
                            for a in range(i - radius, width):

                                # For loop to loop over 0 to (j + radius)
                                for b in range(0, j + radius):

                                    # Get color tuple of pixel (a, b)
                                    pixel = image.getPixel2D(a, b)
                                    
                                    # Accumulate the red, green, and blue
                                    # values
                                    red += pixel[0]
                                    green += pixel[1]
                                    blue += pixel[2]
                                    
                                    # Accumulate count variable
                                    count += 1

                        # Elif statement to check if (j + radius) is larger
                        # than height
                        elif ((j + radius) > height):

                            # For loop to loop over (i - radius) to width
                            for a in range(i - radius, width):

                                # For loop to loop over (j - radius) to height
                                for b in range(j - radius, height):

                                    # Get color tuple of pixel (a, b)
                                    pixel = image.getPixel2D(a, b)
                                    
                                    # Accumulate the red, green, and blue
                                    # values
                                    red += pixel[0]
                                    green += pixel[1]
                                    blue += pixel[2]
                                    
                                    # Accumulate count variable
                                    count += 1

                        # Elif statement to check if (j ± radius) is within
                        # the limits of the frame
                        elif ((j - radius) >= 0) and ((j + radius) <= height):
                        
                            # For loop to loop over (i - radius) to width
                            for a in range(i - radius, width):

                                # For loop to loop over (j ± radius)
                                for b in range(j - radius, j + radius):

                                    # Get color tuple of pixel (a, b)
                                    pixel = image.getPixel2D(a, b)
                                    
                                    # Accumulate the red, green, and blue
                                    # values
                                    red += pixel[0]
                                    green += pixel[1]
                                    blue += pixel[2]
                                    
                                    # Accumulate count variable
                                    count += 1
                                
                # Divide the red, green, and blue sums by count
                red = red / count
                green = green / count
                blue = blue / count
                
                # Set pixel (i, j) to average red, green, and blue values of
                # pixels within radius
                new_image.setPixel2D(i, j, (red, green, blue))

        # Return new_image
        return new_image


# Define scale() function. Scale() function takes a given image and scales it
# up or down depending on a scaling factor, and returns the scaled image.
# Parameters are image and scaling.
def scale(image, scaling):


    # Get width and height of image
    width = image.getWidth()
    height = image.getHeight()
    
    # Calculate new width and height
    new_width = int(width * scaling)
    new_height = int(height * scaling)
    
    # If statement to check if scaling factor is larger than 0
    if scaling > 0:
        
        # Make new empty image with new width and height
        new_image = EmptyImage(new_width, new_height)

        # Get width and height of new empty image
        new_width = new_image.getWidth()
        new_height = new_image.getHeight()

        # Calculate pixel to pixel ratio of original image and new image
        pixel_count = float(1 / scaling)

        # For loop to loop over new width and height
        for i in range(new_width):
            for j in range(new_height):
                
                # Calculate coordinate of pixel in original image
                pixel_width = int(pixel_count * i)
                pixel_height = int(pixel_count * j)
                
                # Get color tuple of pixel
                color = image.getPixel2D(pixel_width, pixel_height)
                
                # Set pixel (i, j) in new image to color found
                new_image.setPixel2D(i, j, color)

        # Return new_image
        return new_image
    
    # Elif statement to check if scaling factor is 0
    elif scaling == 0:
        
        # Return original image
        return image
    
    # Else statement to be executed if scaling factor is less than 0
    else:
        return 'None'


# Define main() function. Main() function asks user for an image and whether
# the user wants to scale, blur, or rotate the image. Returns scaled, blured,
# or rotated image depending on the user's choice. No parameters.
def main():

    
    # Ask user for an image
    image = raw_input('Choose an image: ')

    # Make image object
    image = FileImage(image)
    
    # Ask user if they want to scale, blur, or rotate the image
    choice = raw_input('Do you want to scale, blur, or rotate an image? ')

    # If statement to check whether user wants to scale the image
    if (choice == 'Scale') or (choice == 'scale'):
        
        # Ask user for scaling factor
        scaling = float(raw_input('Enter scaling factor: '))
        
        # Call scale() function. Parameters are image and scaling
        scaled_image = scale(image, scaling)
        
        # If statement to check if scaled_image is not 'None'
        if scaled_image != 'None':
            
            # Show scaled image
            scaled_image.show('Scaled', 10, 10)
        
        # Else statement to be executed if scaled image is 'None'
        else:
            
            # Print scaled image
            print scaled_image

    # Elif statement to check if user wants to blur the image
    elif (choice == 'Blur') or (choice == 'blur'):
        
        # Ask user for bluring radius
        radius = int(raw_input('Enter bluring radius: '))
        
        # Call blur() function. Parameters are image and radius
        blured_image = blur(image, radius)
        
        # If statement to check if blured_image is not 'Invalid radius entered'
        if blured_image != 'Invalid radius entered.':
            
            # Show blured image
            blured_image.show('Blured', 10, 10)
        
        # Else statement to be executed if blured image is 'Invalid radius
        # entered'
        else:
            
            # Print blured image
            print blured_image

    # Elif statement to check if user wants to rotate the image
    elif (choice == 'Rotate') or (choice == 'rotate'):
        
        # Call rotate_left() function. Parameter is image
        rotated_image = rotate_left(image)
        
        # Show rotated image
        rotated_image.show('Rotated to the left', 10, 10)
    
    # Wait for user to admire result
    raw_input('Enter to close')


if __name__ == '__main__':
    main()