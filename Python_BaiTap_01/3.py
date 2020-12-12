a = input("Nhập chuỗi: ")
if (len(a) > 3):
    if(a.endswith('ing')):
        print(a + 'ly')
    else:
        print(a + 'ing')        
else:    
    print(a)
