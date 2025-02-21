from getApi import *

class Cantor():
    def __init__(self):
        self.getApi = GetApi()
        self.firstCurrency = ""
        self.firstValue = 0
        self.secondCurrency = ""
        


    def setFirstCurrencyValueAndSecondCurrency(self):
        currencyList = []
            
        for rate in self.getApi.getCurrencyValue()[0]['rates']:
            code = rate['code']
            currencyList.append(code)
        
        print(currencyList)
        i = 1
        while i:
            setFirstCurrency = input("Podaj walutę(kod): ").upper()
            if setFirstCurrency in currencyList and setFirstCurrency != setFirstCurrency:
                    self.firstCurrency = setFirstCurrency
                    print()
                    while i:
                        getValue = input("Podaj kwotę do wymiany: ")
                        getValue = float(getValue)
                        if getValue > 0:
                            self.firstValue = getValue
                            print()
                            while i:
                                setSecondCurrency = input("Podaj walutę, na którą chcesz wymienić swoje środki: ").upper()
                                if setSecondCurrency in currencyList and setSecondCurrency != setSecondCurrency:
                                    self.secondCurrency = setSecondCurrency
                                    print()
                                    i = 0
                                    break
                                else:
                                    print("podałeś błędny kod waluty... spróbuj ponownie")
                                    self.secondCurrency = None
                        else:
                            print("podałeś kwotę mniejszą od zera.. spróbuj ponownie")
                            self.firstValue = None
            else:
                print("podałeś błędny kod waluty... spróbuj ponownie")
                self.firstCurrency = None
        
   

    def calculation(self):
        currencyValue = self.getApi.getCurrencyValue()

        for rate in currencyValue[0]['rates']:
            code1 = rate["code"]
            val1 = rate ["mid"]
            if code1 == self.firstCurrency:
                break
        for rate in currencyValue[0]['rates']:
            code2 = rate["code"]
            val2 = rate ["mid"]
            if code2 == self.secondCurrency:
                break
        result = self.firstValue * (val1/ val2)
        
        print(result)

c = Cantor ()
c.setFirstCurrencyValueAndSecondCurrency()
c.calculation()