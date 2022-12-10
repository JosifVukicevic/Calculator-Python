import math

def sabiranje(x, y):
    return x + y

def oduzimanje(x, y):
    return x - y

def mnozenje(x, y):
    return x * y

def dijeljenje(x, y):
    return x / y

def kvadratni_korijen(x):
    return math.sqrt(x)

def sinus(x):
    return math.sin(x)

def kosinus(x):
    return math.cos(x)

def stepen(x, y):
    return math.pow(x,y)

print("Odaberite racunsku operaciju: ")
print("1.Sabiranje")
print("2.Oduzimanje")
print("3.Mnozenje")
print("4.Dijeljenje")
print("5.Kvadratni korijen")
print("6.Sinus")
print("7.Kosinus")
print("8.Stepen")

while True:
    operacije = input("Izaberi operaciju(1/2/3/4/5/6/7/8): ")

    if operacije in ('1', '2', '3', '4', '5', '6', '7', '8'):
        prvi_broj = float(input("Unesite prvi broj: "))

        if operacije == '1':
            drugi_broj = float(input("Unesite drugi broj: "))
            print(prvi_broj, "+", drugi_broj, "=", sabiranje(prvi_broj, drugi_broj))

        elif operacije == '2':
            drugi_broj = float(input("Unesite drugi broj: "))
            print(prvi_broj, "-", drugi_broj, "=", oduzimanje(prvi_broj, drugi_broj))

        elif operacije == '3':
            drugi_broj = float(input("Unesite drugi broj: "))
            print(prvi_broj, "*", drugi_broj, "=", mnozenje(prvi_broj, drugi_broj))

        elif operacije == '4':
            drugi_broj = float(input("Unesite drugi broj: "))
            print(prvi_broj, "/", drugi_broj, "=", dijeljenje(prvi_broj, drugi_broj))

        elif operacije == '5':
            print("Korijen broja ", prvi_broj, " je broj => ", round(kvadratni_korijen(prvi_broj),2))

        elif operacije == '6':
            print("Sinus broja ", prvi_broj, " je broj => ", round(sinus(prvi_broj),2))

        elif operacije == '7':
            print("Kosinus broja ", prvi_broj, " je broj => ", round(kosinus(prvi_broj),2))

        elif operacije == '8':
            drugi_broj = float(input("Unesite drugi broj: "))
            print(drugi_broj, " stepen broja ", prvi_broj, " je broj => ", stepen(prvi_broj, drugi_broj))

        sledeca_operacija = input("Zelite li nastaviti sa racunanjem? (DA/NE): ")
        if sledeca_operacija == "NE":
             break
            
        else:
             print("---------------------------------------------------")
