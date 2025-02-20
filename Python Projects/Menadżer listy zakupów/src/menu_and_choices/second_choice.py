import psycopg2
import os


class SecondChoice():
    def __init__(self):
        self.user = "postgres"
        self.password = "admin123"
        self.host = "localhost"
        self.database = "MLZ"
        self.gettingShoppingList = []


    def showCurrentList(self):
        try:
            connection = psycopg2.connect(host = self.host, user= self.user, password = self.password, dbname =  self.database)
            print("--------")
            print("""nawiązano połączenie z bazą\n 
                O to lista Twoich zakupów:
                  """)
            
            cursor = connection.cursor()
            showAll = "SELECT * FROM shopping_list_manager ORDER BY id ASC"

            cursor.execute(showAll)
            result = cursor.fetchall()
            shoppingList = []
            n = 1
            
            
            for i in result:
                shpList = i                
                print(n,". |NAZWA|: "+ shpList[1]+ " |WARTOŚĆ|: "+ shpList[2] + " |KATEGORIA|: " +  shpList[3] )
                shoppingList.append(i)
                n +=1
                print()
            self.gettingShoppingList = shoppingList

            return self.gettingShoppingList
            
        except(Exception,psycopg2.DatabaseError) as error:
            print("Błąd podczas wyświetlania listy", error)    
        finally:
            connection.close()
            cursor.close()
            print("--------")
            print("Zamknięto połączenie z bazą danych")
            print()
    
    def updateData(self):
        self.showCurrentList()

        basicInfo = input("Wybierz numer do zmiany: ")
        num = int(basicInfo)
        
        if num <= len(self.gettingShoppingList):
            num-=1
            getChose = self.gettingShoppingList[num]
            print(getChose)
            print()

            getInfo = input("chcesz zmienić nazwę? 1 - tak, 2 - nie: ")
            getInfo = int(getInfo)
            if getInfo == 1:
                name = input("podaj nową nazwę: ")
            else:
                name = getChose[1]
            
            print()

            getInfo = input("chcesz zmienić wartość?? 1 - tak, 2 - nie: ")
            getInfo = int(getInfo)
            if getInfo == 1:
                value = input("podaj nową wartość: ")
            else:
                value = getChose[2]

            print()

            getInfo = input("chcesz zmienić kategorię?? 1 - tak, 2 - nie: ")
            getInfo = int(getInfo)
            if getInfo == 1:
                category = input("""Podaj nową kategorię. Do wyboru masz:
                    \n- pieczywo,\n- warzywa,\n- owoce,\n- mięso,\n- wędlina,\n- napoje,\n- nabiał:  """ )

                categoryList = ["pieczywo", "warzywo", "owoc", "mięso", "wędlina", "napoje", "nabiał"]

                if category in categoryList:
                    category = category
                
            else:
                    category = getChose[3]

        else:
            print("Podałeś błędny numer")

      
        update = """
                UPDATE shopping_list_manager
                SET name = %s, value = %s, category = %s
                WHERE id = %s
            """
        n = self.gettingShoppingList[num]
        id = n[0]
        self.update(id,name, value,category,update)

        
    


    def update(self,id,name,value,category,update):     
        try:
            connection = psycopg2.connect(host = self.host, user= self.user, password = self.password, dbname =  self.database)
            print("--------")
            print("nawiązano połączenie z bazą")
            cursor = connection.cursor()
           
            cursor.execute(update,(name,value,category,id))
            showAll = "SELECT * FROM shopping_list_manager ORDER BY category ASC"

            cursor.execute(showAll)
            result = cursor.fetchall()
           
            scriptDir = os.path.dirname(__file__)
            os.chdir(scriptDir)

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
            print("Dodano produkt do bazy oraz zakutalizowano plik txt")

        except(Exception,psycopg2.DatabaseError) as error:
            print("Błąd podczas aktualizacji listy", error)    
        finally:
            cursor.close()
            connection.close()

            
            
            print("--------")
            print("Zamknięto połączenie z bazą danych")
            
            



            