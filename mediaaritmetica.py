#pequeno sistema que calcula a média aritmécia
print("Bem-vindos ao sistema de cálculo ")
nome = str(input("Nome do aluno: "))

def calcularMedia(numeros):
    media = sum(numeros)/len(numeros)
    return media

notas = []

for i in range(4):
    valor = float(input("Digite as notas respectivas a cada unidade: "))
    notas.append(valor)

resultado = calcularMedia(notas)

print(f"A média de {nome} é: {resultado}")