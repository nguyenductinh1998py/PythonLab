class Greeter(object):
    def __init__(self, name):
        self.name = name
    def gret(self, loud = False):
        if loud:
            print(f'HELLO, {self.name.upper()}')
        else:
            print(f'Hello, {self.name}')        
g = Greeter('Fred')
g.gret()
g.gret(loud = True)        