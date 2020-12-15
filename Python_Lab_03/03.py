# 3 Hàm

def sign(x):
    if x > 0:
        return 'positive'
    elif x < 0:
        return 'negative'
    else:
        return 'zero'
for x in [-1, 0, 1]:
    print(sign(x))
def hello(name, loud = False):
    if loud:
        print(f'HELLO, {name.upper()}')
    else:
        print(f'hello, {name}')    
hello('Bob')
hello('Fred', loud = True)        
