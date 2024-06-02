try: 

    # get user input
    width = float(input('Enter rectangle width: '))
    length = float(input('Enter rectangel length: '))

    # check if width and length are the same
    if width == length:
        exit('That looks like a square.')

    # calculate area of a rectangle
    area = width * length
    print('The area of the triangle is: ', area)

except ValueError:
    print('Please enter a number!')
    