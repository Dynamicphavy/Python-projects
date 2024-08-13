# Program that can solve both quadratic and simultaneous equations
print('1: Simultaneous Equations')
print('2: Quadratic Equations')
equationType = int(input('What kind of equation do you want to solve?'))
if equationType <= 1:
    a = float(input('X1_'))
    b = float(input('Y1_'))
    c = float(input('C1_'))
    e = float(input('X2_'))
    f = float(input('Y2_'))
    g = float(input('C2_'))
    l = ((a*g)-(e*c))
    m = ((a*f)-b)
    y = l/m
    n = (c-(b*y))
    x = n/a
    print('the value of x =', x, 'and the value of y =', y)
    quit()
else: equationType >= 2
print('This program is to solve quadratic equations')
a = float(input('First integer of your equation_'))
b = float(input('Second integer of your equation_'))
c = float(input('Final integer of your equation_'))
e = (b**2)-(4*a*c)
if e < 0:
    f = (-1*e)**0.5
else:
    f = (e)**0.5
    g = 2*a
    h = ((-b)+f)/g
    i = ((-b)-f)/g
    print('The answer to the quadratic equation is', i, 'and', h)