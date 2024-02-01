while True:
    print("adiciunar=1")
    print("subtrair=2")
    print("multiplicar=3")
    print("dividir=4")
    print("calcular putencia=5")
    print("calcular resto da divisão=6")
    print("calcular par ou impar=7")

    option = int(input("insira a opçao que precise: "))

    if option == 1:
        n1 = float(input("insira o numero: "))
        n2 = float(input("insira o numero: "))
        print(n1 + n2)

    elif option == 2:
        n1 = float(input("insira o numero: "))
        n2 = float(input("insira o numero: "))
        print(n1 - n2)

    elif option == 3:
        n1 = float(input("insira o numero: "))
        n2 = float(input("insira o numero: "))
        print(n1 * n2)

    elif option == 4:
        n1 = float(input("insira o numero: "))
        n2 = float(input("insira o numero: "))
        print(n1 / n2)

    elif option == 5:
        n1 = float(input("insira o numero: "))
        n2 = float(input("insira o numero: "))
        print(n1 ** n2)

    elif option == 6:
        n1 = float(input("insira o numero: "))
        n2 = float(input("insira o numero: "))
        print(n1 % n2)

    elif option == 7:
        n1 = int(input("insira o numero: "))

        resultado = n1 % 2

        if resultado == 0:
            print("par")

        elif resultado <= 1:
            print("impar")

    else:
        print("opçao invalida tente mais tarde")
