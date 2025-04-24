"""
Exercicio 8 - Primeira Letra em Maiúscula
Descrição: Peça uma palavra e exiba-a com a primeira letra maiúscula.

"""

#Solicitamos uma string ao usuario e armazenamos na variavel palavra.
palavra = input("Digite uma palavra: ")


#Imprimimos na tela a frase abaixo e a palavra com a primeira letra maiuscula.
print(f"Você disse a palavra { palavra.capitalize()}")

#OBS: O método utilizado ira nos ajudar na prosposta do exercicio.
# .capitalize() = Esse método tranforma a primeira letra da string fornecida em maiscula e as demais em minusculas. 