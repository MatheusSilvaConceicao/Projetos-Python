"""
Exercicio 9 - Último Dígito de um Número
Descrição: Peça ao usuário um número inteiro e exiba seu último dígito.

"""
#Solicitamos um número inteiro ao usuário
numero = int(input("Digite um número: "))

#Imprimimos na tela o ultimo digito utilizando o operador modulo.
print(f"O último dígito do seu número é: {numero % 10}")