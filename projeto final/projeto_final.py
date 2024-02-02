def somar(n1, n2):
    return n1 + n2

def subtrair(n1, n2):
    return n1 - n2


def multlipicar(n1, n2):
    return n1 * n2


def dividir(n1, n2):
    return n1 / n2

while True:
    lista = ["somar1", "subtrair2", "multiplicar3", "dividir4", "potencia5", "resto da divisao6", "par ou impar7"]
    for elementos in lista:
        print(elementos)
    option = int(input("insira a opçao que precise: "))

    if option == 1:
        n1 = float(input("insira o numero== "))
        n2 = float(input("insira o numero== "))

        print(somar(n1, n2))

    elif option == 2:
        n1 = float(input("insira o numero== "))
        n2 = float(input("insira o numero== "))

        print(subtrair(n1, n2))

    elif option == 3:
        n1 = float(input("insira o numero== "))
        n2 = float(input("insira o numero== "))

        print(multlipicar(n1, n2))

    elif option == 4:
        n1 = float(input("insira o numero== "))
        n2 = float(input("insira o numero== "))

        print(dividir(n1, n2))

    elif option == 5:
        n1 = float(input("insira o numero== "))
        n2 = float(input("insira o numero== "))
        print(n1 **n2)

    elif option == 6:
        n1 = float(input("insira o numero== "))
        n2 = float(input("insira o numero== "))
        print(n1 % n2)

    elif option == 7:
        n1 = int(input("insira o numero== "))
        resultado = n1 % 2
        if resultado == 0:
            print("par")
        elif resultado <= 1:
            print("impar")

    else:
        pass