"""
Exercicio 6 - Tipos de Dados
Descrição: Peça ao usuário para inserir um valor e mostre o tipo desse valor usando type().

"""

#Solicitamos um valor ao usuario e guardamos ele na variavel valor.
valor = input("Digite um valor: ")

#Imprimimos na tela a mensagem abaixo mostrando o valor que ele inseriu e o seu tipo usando o metodo type()
print(f"Você digitou {valor} e ele é do tipo {type(valor)}")
