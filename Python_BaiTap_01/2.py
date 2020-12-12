n = int(input("Bạn muốn list có bao nhiêu số: "))
lst = []
a = ''
for i in range(n):
    lst.append(input())
for i in lst:
    a += i
b = int(a)    
print(b)

