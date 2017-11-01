from quiz import Quiz


class Menu:

    def __init__(self):
        self._quiz = Quiz()
        self._choice = None

    def mainMenu(self):

        loop = True
        while loop:
            self.mainMenuTxt()

            inpt = input("Input: ")

            if inpt == '1':
                self.allRandom()
            if inpt == '2':
                self.kategorier()

    def mainMenuTxt(self):
        print("1: Start All Random \n")
        print("2: Start Kategorier \n")
        print("(Q)uit \n")
        print("\n")
        #print("Andrea & Ketil (c) 2017")
        print("\n")

    def allRandom(self):
        self._quiz.clear_screen()
        self._quiz.lesFraFil("questions.txt")
        self._quiz.printQuestion()
        inpt = ""
        while inpt != 'q':
            self.allRandomTxt()
            inpt = input("Input: ")
            self._quiz.clear_screen()

            #Get answer
            if inpt == "1":
                self._quiz.getAnswer()
            #Save for later
            elif inpt == "2":
                pass
            #Neste
            elif inpt == "3":
                self._quiz.clear_screen()
                self._quiz.getAvailableQs()
                self._quiz.printQuestion()

            #Return
            elif inpt == "4":
                break

    def allRandomTxt(self):
        print("\n")
        print("1: Vis svar")
        print("2: Ta vare på til senere")
        print("3: Neste")
        print("4: Tilbake")
        print("\n")

    def kategorier(self):
        self._quiz.clear_screen()
        print("Kategorier: ")
