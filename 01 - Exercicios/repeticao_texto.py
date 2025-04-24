"""
Exercicio 10 - Repetição de Texto
Descrição: Peça ao usuário uma palavra e um número n. Exiba a palavra repetida n vezes.

"""
#Imprimimos na tela o objetivo exercicio
print("====== Repetição de texto ======")

#Solicitamos a palavra ao usuario
palavra = input("Digite uma palavra: ")

#Solicitamos quantas vezes sera repetida
n = int(input("Quantas vezes você quer repetir essa palavra: "))

#Imprimimos na tela a quantidade de vezes
print(f"{palavra * n}")