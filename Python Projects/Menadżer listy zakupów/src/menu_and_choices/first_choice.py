import os
import psycopg2

class FirstChoice():
    def __init__(self):
        self.shoppingList = {}
        self.categoryList = ["pieczywo", "warzywa", "owoce", "mięso", "wędlina", "napoje", "nabiał"]
        self.category = ""
        self.i = 0
    
    def cleanTable(self):
        user = "postgres"
        password = "admin123"
        host = "localhost"
        database = "MLZ"
        try:
            connection = psycopg2.connect(host = host, user=user, password = password, dbname = database)
            print("--------")
            print("nawiązano połączenie z bazą")
            cursor = connection.cursor()
            clean = "TRUNCATE TABLE shopping_list_manager"
            
            cursor.execute(clean)
            
            connection.commit()
            print("--------")
            print("Wyczyszczono bazę")

        except(Exception,psycopg2.DatabaseError) as error:
            print("Błąd podczas czyszczenia bazy", error)    
        finally:
            connection.close()
            cursor.close()
            print("--------")
            print("Zamknięto połączenie z bazą danych")

    def createNewCategory(self):
        i = True
        while i:
            firstMenu =("""Wpisz kategorię, do której będziesz dodawał produkty. Do wyboru masz:
                                        \n- pieczywo,\n- warzywa,\n- owoce,\n- mięso,\n- wędlina,\n- napoje,\n- nabiał: """)
            print(firstMenu)
            choice = str(input().lower())
            
            if choice in self.categoryList:
                self.category = choice
                i = False
                
            else:
                print("UPS! wybrałeś błędną kategorię :(, spróbuj ponownie")
        
        return False
            

       
    
    def addProductToShoppingList(self):
        if self.category not in self.shoppingList:
                self.shoppingList[str(self.category)] = []
        

        if self.category in self.shoppingList:
            while True:
                pr = input("podaj nazwę produktu: ")
                val = input("podaj wagę/ ilość: ")
                cat = self.category
                
                user = "postgres"
                password = "admin123"
                host = "localhost"
                database = "MLZ"
                try:
                    connection = psycopg2.connect(host = host, user=user, password = password, dbname = database)
                    print("--------")
                    print("nawiązano połączenie z bazą")
                    cursor = connection.cursor()
                    add = """
                        INSERT INTO shopping_list_manager (name, value, category)
                        VALUES(%s,%s,%s)
                    """
                    cursor.execute(add,( pr, val, cat))
                    product = f"Nazwa: {str(pr)}" +f" Waga/ Ilość: {str(val)}"
                    self.shoppingList[self.category].append(product)

                    showAll = "SELECT * FROM shopping_list_manager ORDER BY category ASC"

                    cursor.execute(showAll)
                    result = cursor.fetchall()
                
                    os.chdir("./")

                    fh = open("lista.txt", "w", encoding="utf-8")
                
                    x = 0
                    for i in result:
                        shpList = i                
                        print(x,". |NAZWA|: "+ shpList[1]+ " |WARTOŚĆ|: "+ shpList[2] + " |KATEGORIA|: " +  shpList[3] )
                        fh.write(". |NAZWA|: "+ shpList[1]+ " |WARTOŚĆ|: "+ shpList[2] + " |KATEGORIA|: " +  shpList[3] + "\n")
                        x +=1
                        print()

                    fh.close()
                    
                    connection.commit()
                    print("--------")
                    print("Dodano produkt do bazy")

                except(Exception,psycopg2.DatabaseError) as error:
                    print("Błąd podczas tworzenia", error)    
                finally:
                    connection.close()
                    cursor.close()
                    print("--------")
                    print("Zamknięto połączenie z bazą danych")


                print()
                con = input( "Chcesz dodać kolejny? wcisńij '1, Chcesz zmienić kategorię? wciśnij '2', jeśli natomiast chcesz zakończyć i wrócić do menu głównego wybierz '0': ")
                print("""\n


                    """)
                if con == "2":
                    self.set_I(2)
                    break
                if con == "0":
                    self.set_I(0)
                    break
        
        return False
       
    @property
    def get_I(self):
        return self.i
    
    
    def set_I(self, newI):
        if not isinstance(newI, int):
            raise ValueError("I musi być liczbą całkowitą")
        self.i = newI
    
    @property
    def get_ShoppingList(self):
        return self.shoppingList
    
