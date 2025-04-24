"""
Par ou Ímpar: Peça para o usuário inserir um número e use uma estrutura condicional para verificar se ele é par ou ímpar.

"""

n = int(input("Digite um número: "))


if(n % 2 == 0):
    print(f"Você digitou {n} e ele é um número par.")
else:
    print(f"Você digitou {n} e ele é um número impar.")
    
    