while True:

    idade = int(input("qual a sua idade ="))

    if idade >= 18:
        print("pode voter")

    elif idade < 18 and idade > 0:
        print("não pode votar")

    elif idade < 0:
        print("não pode ter menos que zero")

    else:
        print("tente mais tarde")
























