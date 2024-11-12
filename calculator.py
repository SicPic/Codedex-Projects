print('AREA CALCULATOR')

print('1) Triangle')
print('2) Rectangle')
print('3) Square')
print('4) Circle')
print('5) Quit')
shape = int(input('Which shape do you choose?'))

side = 0
length = 0
width = 0
heigth = 0
radius = 0
base = 0

if shape == 1:
    base = int(input('Base:'))
    heigth = int(input('Heigth:'))
    print('The area is:', (heigth * base) / 2 )
elif shape == 2:
    length = int(input('Length:'))
    width = int(input('Width:'))
    print('The area is:', length * width)
elif shape == 3:
    side = int(input('Side:'))
    print('The area is:', side ** 2)
elif shape == 4:
    radius = int(input('Radius:'))
    print('The area is:', 3.14 * (radius ** 2))
else:
    print('Thank you for participating!')

