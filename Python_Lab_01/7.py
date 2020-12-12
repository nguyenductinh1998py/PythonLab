n = int(input("Nhập n đề liệt kê các sos nguyên tố trước nó : "))
def soNT(i):
    count = 0
    for s in range(1, i + 1):
        if (n % s == 0):
            count += 1
    if count == 2:
        print(s)
for n in range(2, n + 1):
    if n == 1:
        print(1)
    soNT(n)