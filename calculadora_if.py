print("adiciunar=1")
print("subtrair=2")
print("multiplicar=3")
print("dividir=4")
print("sair=5")

option = int(input("insira a opçao que precise: "))

if option == 1:
    n1 = int(input("insira o numero: "))
    n2 = int(input("insira o numero: "))
    print(n1 + n2)

elif option == 2:
    n1 = int(input("insira o numero: "))
    n2 = int(input("insira o numero: "))
    print(n1 - n2)

elif option == 3:
    n1 = int(input("insira o numero: "))
    n2 = int(input("insira o numero: "))
    print(n1 * n2)

elif option == 4:
    n1 = int(input("insira o numero: "))
    n2 = int(input("insira o numero: "))
    print(n1 / n2)

elif option == 5:
    pass

else:
    print("opçao invalida tente mais tarde")
