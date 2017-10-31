from quiz import Quiz

def main():

    #Oppretter objekt av Quiz
    quiz = Quiz()

    #Rydder skjermen
    quiz.clear_screen()

    #Mah loop
    loop = True

    #inpt = input("Input: ")
    while loop:

        #Hovedmeny
        print("1: Start All Random \n")
        print("2: Start Kategorier \n")
        print("(Q)uit \n") #Should be consistent in menu

        inpt = input("Input: ")

        #All Random
        if inpt == '1':
            quiz.clear_screen()
            quiz.lesFraFil("questions.txt")
            quiz.printQuestion()
            quiz.getQuestion()
            while inpt != 'q':

                #All Random meny
                print("\n")
                print("1: Vis svar")
                print("2: Ta vare på til senere")
                print("3: Neste")
                print("4: Tilbake")
                print("\n")

                inpt = input("Input: ")
                quiz.clear_screen()

                #Get answer
                if inpt == "1":
                    quiz.getAnswer()
                #Save for later
                elif inpt == "2":
                    pass
                #Neste
                elif inpt == "3":
                    quiz.clear_screen()
                    quiz.lesFraFil("questions.txt") #Kjøres to ganger?
                    quiz.printQuestion()
                    quiz.getQuestion()
                #Return
                elif inpt == "4":
                    break

        #Kategorier
        elif inpt == 2:
            quiz.clear_screen()
            print("Kategorier: ")
        #Quit
        elif inpt.lower() == 'q':
            loop = False
        #Unknown input
        else:
            print("I didn't understand that. Please try again.")

main()


##Stuff to do########################################################
# Kategorier                                                        #
# Fylle ut spørsmålsliste                                           #
# Se om vi får til å lage GUI mer sexy                              #
# Hindre å gi samme spørsmål flere ganger                           #
# Snakke om Way of Kings
