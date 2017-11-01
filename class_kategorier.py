class Kategorier:
    def __init__(self, tekstfil):
        self._sporsmaal = None
        self._svar = None
        self._kategorier = open(tekstfil, 'r')
        self._spurt = []
        self._kategorivalg = None


    def lesKategorier(self):
          for linje in self._kategorier:
              if linje[0] == '*':
                  print(linje[1:])
          self._kategorivalg = input('Velg kategori: ')
          return self._kategorivalg

    def hentKategorisporsmaal(self):
        #for linje in self._kategorier:
        for linje in open('kategorier.txt', 'r'):
            #if linje[0] == self.lesKategorier()
            if linje[0] == self._kategorivalg:
                biter = linje.split(':')
                self._sporsmaal = biter[0]
                self._svar = biter[1]

    def printSporsmaal(self):
        if self._sporsmaal not in self._spurt:
            print(self._sporsmaal[1:])
        self._spurt.append(self._sporsmaal)

    def printSvar(self):
        print(self._svar)




#kat = Kategorier('kategorier.txt')
#kat.lesKategorier()
#kat.hentKategorisporsmaal()
