from menu_and_choices.first_choice import FirstChoice
from menu_and_choices.second_choice import SecondChoice
from menu_and_choices.thirdd_choice import ThirdChoice
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
              \n3. wyeksportować to pliku txt najaktualniejszą listę
              \n4. wyjść
               """)
        
    
        
    def logicChoice(self):
        info = input("Co wybierasz?")

        if info == "1":
            q = input("chcesz usunąć poprzednią listę?: 1. tak, 2. nie: ")
            q = int(q)
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

                info = input("chcesz zmienić coś jescze? 1. tak, 2. nie: ")
                info = input(info)

                if info == 1:
                    return True
                elif info == 2:
                    break
                else:
                    pass

        elif info == "3":
            self.thirdChoice.getActualList()

        elif info == None:
            print("dziękujemy za skorzystanie z menadżera listy")




           



        

        
       


                

        
            
            