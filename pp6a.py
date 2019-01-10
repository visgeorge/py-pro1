class Pen:
    def __init__(self,name,colour):
        self.name=name
        self.colour=colour
        self.ink_lvl=100

    def write(self,words):
        print('\nWriting "',words,'"',end=' ')
        print('with',self.name,'in',self.colour,'ink')
        self.ink_lvl-=20


    def ink_left(self):
        print('\n',self.name,'has',self.ink_lvl,'% ink remaining')

