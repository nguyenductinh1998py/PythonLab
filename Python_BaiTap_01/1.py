str_a = input("Nhập chuỗi: ")
lst = str_a.split(" ")
lst1 = []
for i in lst:
    if len(i) > 3:
        lst1.append(i)
print(lst1)        