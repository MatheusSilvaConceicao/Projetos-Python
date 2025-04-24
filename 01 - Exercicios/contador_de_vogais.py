"""
5 - Contador de Vogais:
Descrição: Peça ao usuário que insira uma palavra e conte quantas vogais ela contém.
Objetivo: Manipular strings e utilizar estruturas de repetição.

"""
#Declaramos uma variavel que vai receber uma palavra do usuário.
palavra = input("Digite uma palavra: ")

#Declaramos uma variavel que contem as vogais do alfabeto para verificação posterior.
vogais = "aeiou"

#Declaramos uma variavel que vai funcionar como um contador, inicializando no 0.
contador = 0;

""" Estrutura de Repetição """
#Começamos um for que vai iterar sobre a variavel palavra
for letra in palavra:
    
#Iniciamos um if que a cada iteração do for vai verificar se a letra é uma vogal, caso seja ele adiciona 1 ao contador.
    if letra in vogais:
        
        
        contador += 1

#Imprimimos na tela o resultado dessa estrutura ao usuário informando a palavra e a quantas vogais possui.      
print(f"A palavra {palavra} contém {contador} vogais.")
