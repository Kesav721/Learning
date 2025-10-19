#Q Function to find area of a circle (radius is positional argument)

def area_circle(r):
    pi=3.14
    return pi*r*r

r=float(input('Enter the radius :'))

print('Area of the circle is :',area_circle(r))
