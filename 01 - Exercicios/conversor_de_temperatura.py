"""
3 - Conversor de Temperatura:
Descrição: Crie um programa que converta uma temperatura de graus Celsius para Fahrenheit.
Objetivo: Praticar operações matemáticas e manipulação de variáveis do tipo float.

"""

#Declaramos a variavel abaixo que recebe o valor a ser convertido.
celsius = float(input("Qual o valor da temperatura que você deseja converter para Fahrenheit: "))

#Declaramos a variavel abaixo que converter o valor solicitado. 
fahrenheit = (celsius * 1.8) + 32

#Imprimimos o valor na tela para o usuário.
print(f"{celsius}C° são {fahrenheit}°F")
