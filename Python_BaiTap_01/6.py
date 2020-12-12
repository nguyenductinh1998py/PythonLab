n = int(input("Bạn muốn list có bao nhiêu số: "))
lst = []
for i in range(n):
    lst.append(int(input()))
lst1 = [x for x in lst if x % 2 ==0]    
print(lst1)