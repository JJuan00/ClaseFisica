from numpy import array, pi, sin
from itertools import combinations
# from array import array

class Principal:

    def combinacionAndFormula(self, arrayNum):
        constK = 8990000000
        arrayQ = []
        tempQ = []
        combinacionesQ = []
        C = 0
        tempNumQ = len(arrayNum)
        while True:
            arrayQ.append(tempNumQ)
            tempNumQ -= 1
            if tempNumQ == 0:
                break
        for item in reversed(arrayQ):
            tempQ.append(item)

        quality = int(input("Cuantas combinaciones necesita"))
        if quality > 0:
            # while True:
                # v1 = int(input("Primer numero Q1 -> "))
                # v2 = int(input("Primer numero Qn -> "))
                for x in combinations(tempQ, 2):
                    # if x == (v1, v2): 
                        print(x)
                # if C == quality:
                #     break
        else:
            print("No necesita combinaciones.")



    def datos(self):
        arrayNum = []
        print("\nSolo halla la Fn")
        numeroPuntosQ = int(input("Ingrese cantidad de numeros de Q**1, Q**2... Q**n -> "))
        Count = 0
        if numeroPuntosQ >= 2:
            while True:
                numOpcion = int(input("1. Decimal\n2. Entero\n-> "))
                if numOpcion == 1:
                    numDecimal = float(input("Ingrese numero Q%d -> " % (Count + 1)))
                    arrayNum.append(numDecimal)
                    # i = i + 1
                elif numOpcion == 2:
                    numEntero = int(input("Ingrese numero Q%d -> " % (Count + 1)))
                    arrayNum.append(numEntero)
                    # j = j + 1
                Count += 1
                if Count == numeroPuntosQ:
                    break
            self.combinacionAndFormula(arrayNum)
        else:
            print("Mal")
       

if __name__ == "__main__":
    Main = Principal()
    Main.datos()