from random import randint

class Kategorier:
    def __init__(self, tekstfil):
        self._kategoriNummer = []
        self._alleKategorier = []
        self._asked = []
        self._tekstfil = open('kategorier.txt', 'r')
        self._kategorivalg = 0


    def appendKategorier(self):


        #while self._kategoriNummer == None:
        for linje in open('kategorier.txt'):
            midList = []
            sporsmaal = []
            svar = []
            #print(linje)
            if linje[0][0] == '*':
                midList.append(int(linje[2]))
                nummer = linje[2]
                #for linje in open('kategorier.txt'):
            if linje[0][0] == nummer:
                linje = linje[1:]
                biter = linje.split(':')
                sporsmaal.append(biter[0])
                svar.append(biter[1])
                midList = [sporsmaal, svar]
                self._alleKategorier.append(midList)




        print(self._alleKategorier)

        for i in self._alleKategorier:
            print('\n')
            print(i)



                #self._kategoiNummer.append(forste)
                #print(self._kategoriNummer)

    def appendSporsmaalSvar(self):
        sporsmaal = []
        svar = []
        for linje in open('kategorier.txt', 'r'):
            #print(linje)
            if linje.strip() == self._kategoriNummer:
                #if linje[0] == self.lesKategorier()
                linje = linje[1:]
                biter = linje.split(':')
                sporsmaal.append(biter[0])
                svar.append(biter[1])
                self._ordIkategorier.append(sporsmaal)
                self._ordIkategorier.append(svar)
                self._alleKategorier.append(self._ordIkategorier)
                #print('2', self._alleKategorier)
                self._ordIkategorier = []
                #print('3', self._ordIkategorier)



    def kategoriAlternativer(self):
        return self._alleKategorier

    def returnKategorivalg(self, kategorivalg):
        for element in self._alleKategorier:
            if element == kategorivalg:
                self._kategorivalg = kategorivalg

    def returnSporsmaal(self):
        for element in self._alleKategorier:
            if element == self._kategorivalg():
                return element[0]


    def returnSvar(self):
        for element in self._alleKategorier:
            if element[0] == self._kategorivalg():
                return element[1]

'''
    def getRandIndex(self):
        x = randint(0, (len(self.returnSporsmaal())-1))
        return x

    def getIndex(self):
        x = self.dontShowAgain()
        self._asked.append(x)
        return x

    def getSporsmaal(self):
        x = self.getIndex()
        return self.returnSporsmaal[x]

    def getSvar(self):
        x = self.getIndex()
        return self.returnSvar[x]

    def dontShowAgain(self):
        i = self.getRandIndex()
        while i in self._asked:
            i = self.getRandIndex()
        #self._asked.append(i)
        return i

    def getAvailableQs(self):
        if len(self.returnSporsmaal) == len(self._asked):
            print("No more questions left")
            self.returnToMenu()

    def returnToMenu(self):
        inpt = input("Press Enter to return to menu")
        if inpt == "":
            print("Her skal man egentlig hoppe tilbake til menyen.")
'''
'''
    def returnLenSporsmaal(self):
        return len(self._alleKategorier[self._kategorivalg[0]])

    def returnLenSporsmaal(self):
        element = 0
        for element in self._alleKategorier:
            return len(self._alleKategorier[self._kategorivalg[0[element]]])
            element += 1

'''
''''''
kat = Kategorier('kategorier.txt')
kat.appendKategorier()
kat.appendSporsmaalSvar()
#kat.returnKategorivalg(1)
kat.returnSporsmaal()
kat.returnSporsmaal()

#print(kat.getSporsmaal())
#print(kat.getSvar())
