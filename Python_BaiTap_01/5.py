n = int(input("Nhập n:  "))
a = 0
if(n > 1):
    if(n == 2 or n == 3):
        print(1)
    else:
        for i in range(1,int(n / 2) + 1):
            if(n % i == 0):
                a += i
else:
    print("1 Không có ước số")    
if(a > n):
    print(False)
else:
    print(True)    
