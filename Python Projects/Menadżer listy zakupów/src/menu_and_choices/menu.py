from menu_and_choices.first_choice import FirstChoice
from menu_and_choices.second_choice import SecondChoice
from menu_and_choices.third_choice import ThirdChoice
class Menu:
    def __init__(self):
        self.notDone = True
        self.firstChoice = FirstChoice()
        self.secondChoice = SecondChoice()
        self.thirdChoice = ThirdChoice()

    def mainMenu(self):
        print("""######### Menu główne #########  
              \nCo chcesz zrobić?
              \n1. utworzyć nową listę zakupów
              \n2. zaktualizować istniejącą listę
              \n3. wyświetlić aktualną listę
              \n4. wyjść
               """)
        
    
        
    def logicChoice(self):
        while True:
            print()
            self.mainMenu()
            info = input("Co wybierasz?: ")

            if info == "1":
                q = input("chcesz usunąć poprzednią listę?: 1. tak, 2. nie: ")
                try:
                    q = int(q)
                except ValueError:
                        print()
                        print("Nie można przekonwertować na liczbę całkowitą")
                        print()
                
                if q == 1:    
                    self.firstChoice.cleanTable()
                
                while self.notDone:
                    while True:
                        self.firstChoice.createNewCategory()
                        break   
                    if True:
                        while self.notDone:
                            self.firstChoice.addProductToShoppingList()
                            if self.firstChoice.get_I == 2:
                                break
                            elif self.firstChoice.get_I == 0:
                                self.notDone = False

            elif info == "2":
                while True:
                    self.secondChoice.updateData()
                    print()
                    info = input("chcesz zmienić coś jescze? 1. tak, 2. nie: ")
                    try:
                        info = int(info)
                    except ValueError:
                        print()
                        print("Nie można przekonwertować na liczbę całkowitą")
                        print()
                    
                    if info == 1:
                        return True
                    elif info == 2:
                        break
                    else:
                        pass

            elif info == "3":
                self.thirdChoice.getActualList()
                continue

            elif info == "4":
                print("dziękujemy za skorzystanie z menadżera listy")
                break
            else:
                continue




           



        

        
       


                

        
            
            