import pp6a

class Gelpen(pp6a.Pen):
    def quality(self):
        print(self.name,"writes smooth")

jif=Gelpen('Jiffy','Black')

jif.quality()

jif.write('Hello good morning')

jif.ink_left()

jif.write('Bye')






