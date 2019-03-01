from math import exp, expm1

def form__coulumb():
    constanteK = 8.99*10**9
    # microCoulomb = "e-6"
    x = float(input("Ingrese primer Q -> "))
    y = int(input("Ingrese segunda Q -> "))
    z = float(input("Ingrese distancia -> "))
    x1 = x*10**-6
    y1 = y*10**-6
    aplicatiElecQ = ((x1) * (y1))
    z = z ** 2
    newResult = (constanteK * aplicatiElecQ)
    result = (newResult / z)
    print(result)
    

if __name__ == "__main__":
    try:
        c = 0
        numRepetition = int(input("Ingrese la cantidad de veces a calcular la fuerza -> "))
        while True:
            form__coulumb()
            if c == numRepetition:
                break

    except numRepetition:
        print("Error 24")