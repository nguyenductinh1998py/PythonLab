a = int(input('Nhập số a: '))
b = int(input('Nhập số b: '))
c = int(input('Nhập số c: '))
if(a == b == c):
    print('Euqilateral triangle')
if(a == b or a == c or b == c):
    print('Isosceles triangle')  
if(a != b != c):
    print('Scalene triangle')  