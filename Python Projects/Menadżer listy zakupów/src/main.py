import time
from menu import *
from product import *
        
        
menu = Menu()
product = Product()
while True:
    product.choiceCategory()
    product.addProduct()
    product.addValue()
    product.addProductToList()
    time.sleep(1)
    product.exportListToTxtFile()
    


