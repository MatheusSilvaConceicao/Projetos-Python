"""
2 - Calculo da idade:
    Descrição: Solicite ao usuário o ano do seu nascimento e calcule sua idade atual.
    Objetivo: Trabalhar com operções aritméticas e manipulação de números.

"""
#Declaramos a variavel ano que recebe o ano de nascimento do usuário.
ano = int(input("Qual ano você nasceu: "))

#Recebemos o valor da variavel ano e subtraimos do ano atual colocando o valor na variavel idade.
idade = 2025 - ano

#Imprimimos na tela a mensagem mostrando a idade do usuário.
print(f"Você nasceu em {ano} e tem {idade} anos de idade.")

