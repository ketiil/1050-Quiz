from random import randint
from os import system as execute
from platform import system as checkOS

class Quiz:



    def __init__(self,):
        self._question = []
        self._answer = []
        self._asked = []
        #self._ordbok = {}
        #self._teller = 0

    def lesFraFil(self, filnavn):
        quiz = open(filnavn, "r")
        for i in quiz:
            biter = i.split(";")
            question = biter[0]
            answer = biter[1].strip()
            self._question.append(question)
            self._answer.append(answer)
            #self._ordbok[question] = answer


    def getRandIndex(self):
        x = randint(0, (len(self._question)-1))
        return x

    #Get question
    def getQuestion(self):
        #i = self.getRandIndex()
        #self._asked.append(i)
        x = self.dontShowAgain()
        self._asked.append(x)
        return self._question[x]

    #Print question
    def printQuestion(self):
        print(self.getQuestion())

    #Get answer
    def getAnswer(self):
        i = self._asked[-1]
        print(self._answer[i])

    def dontShowAgain(self):
        i = self.getRandIndex()
        while i in self._asked:
            i = self.getRandIndex()
        #self._asked.append(i)
        return i

    def getAvailableQs(self):
        if len(self._question) == len(self._asked):
            print("No more questions left")
            self.returnToMenu()

    def returnToMenu(self):
        inpt = input("Press Enter to return to menu")
        if inpt == "":
            print("Her skal man egentlig hoppe tilbake til menyen.")


    def saveForLater(self):
        pass

    def kategorier(self):
        pass #heihei

    def clear_screen(self):
        os = checkOS()
        if os == "Windows":
            execute("cls")
        else:
            execute("clear")

            #hei
