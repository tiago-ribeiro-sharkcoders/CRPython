nomeficheiro = "teste.txt"

# escrever no ficheiro sem overwrite (append)
ficheiro = open(nomeficheiro, "w")
ficheiro.write("ola")
ficheiro.close()

nome = input ("ponha o seu nome")

ficheiro = open(nomeficheiro, "a")
ficheiro.write(f"ola {nome}")
ficheiro.close()

# ler ficheiro
ficheiro = open(nomeficheiro, "r")
conteudo = ficheiros.read()
print(conteudo)
ficheros.close()
