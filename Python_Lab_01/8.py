def soNT(i):
    count = 0
    for s in range(1, i + 1):
        if (n % s == 0):
            count += 1
    if count == 2:
        print(s)
for n in range(10000, 99999 + 1):
    soNT(n)