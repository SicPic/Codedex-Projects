print('AREA CALCULATOR')

while True:
    print('1) Triangle')
    print('2) Rectangle')
    print('3) Square')
    print('4) Circle')
    print('5) Quit')

    shape = int(input('Which shape do you choose? '))

    if shape == 1:
        base = int(input('Base: '))
        height = int(input('Height: '))
        print('The area is:', (height * base) / 2)
    elif shape == 2:
        length = int(input('Length: '))
        width = int(input('Width: '))
        print('The area is:', length * width)
    elif shape == 3:
        side = int(input('Side: '))
        print('The area is:', side ** 2)
    elif shape == 4:
        radius = int(input('Radius: '))
        print('The area is:', 3.14 * (radius ** 2))
    elif shape == 5:
        print('Thank you for participating!')
        break
    else:
        print('Please enter a valid value.')

