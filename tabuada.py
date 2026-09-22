numero = int(input("Digite o número da tabuada: "))

for i in range(10):
    tabuada  = numero * (i + 1)
    print(f"{numero} X {i + 1} = {tabuada}")

