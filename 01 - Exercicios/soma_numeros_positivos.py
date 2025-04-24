#Leia 5 números, some apenas os positivos

i = 0
lista = []
positivo = []
negativo = []

while i < 5:
    valor = int(input(f"Digite o número {i+1}/5 : "))
    lista.append(valor)
    if valor > 0:
        positivo.append(valor)    
    else:
        negativo.append(valor)
    i += 1    

print(f"Esses são os números digitados: {lista}")
print(f"Esses são os valores positivos da lista: {positivo} e sua soma {sum(positivo)}")
print(f"Esses são os valores negativos da lista: {negativo}")

