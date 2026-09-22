print("Olá! Escolha em qual base númerica você deseja trasnformar o número. ")
print("Digite 1 - para binário. ")
print("Digite 2 - para octal. ")
print("Digite 3 - para hexadecimal")

escolha = int(input("Digite sua escolha: "))

if escolha not in (1, 2,3):
    print("Escolha um número de 1 a 3")
else:
    numero = int(input("Digite um número: "))

    if escolha == 1:
            opcao = str(input("Deseja transformar{} em binário? Digite 'Sim' para confirmar e 'Não' para cancelar ".format(numero)))
            if opcao == "Sim":
                numero_binario = bin(numero)[2:]
                print("O número {} em binário é igual a {}".format(numero, numero_binario))
            else:
                print("Escolha outra opção")
    elif escolha == 2:
            opcao =  str(input("Deseja transformar{} em octal? Digite 'Sim' para confirmar e 'Não' para cancelar ".format(numero)))
            if opcao == "Sim":
                numero_octal = oct(numero)[2:]
                print("O número {} em octal é igual a {}".format(numero, numero_octal))
            else:
                print("Escolha outra opção")
    else:
            opcao =  str(input("Deseja transformar{} em hexadecimal? Digite 'Sim' para confirmar e 'Não' para cancelar ".format(numero)))
            if opcao == "Sim":
                numero_hexa = hex(numero)[2:]
                print("O número {} em hexadecimal é igual a {}".format(numero, numero_hexa))
            else:
                print("Escolha outra opção")