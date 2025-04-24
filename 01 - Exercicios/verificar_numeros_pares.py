"""
4 - Verificador de Números Pares:
Descrição: Solicite um número inteiro ao usuário e informe se ele é par ou ímpar.
Objetivo: Utilizar operadores condicionais e estruturas de controle de fluxo.

"""

#Declaramos um variavel que solicita um número inteiro ao usuário
num = int(input("Digite um número: "))

#Estruturas de condição
""" 
Verifica se resto do número dividido por 2 é igual a zero, caso seja ele imprimi o primeiro print, caso não ele imprimi o segundo print.
"""

if(num % 2 == 0):
    print(f"Você digitou {num} e ele é par")
else:
    print(f"Você digitou {num} e ele é impar")