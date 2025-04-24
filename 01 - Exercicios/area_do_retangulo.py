"""
Exercicio 7 - Área de um Retângulo
Descrição: Solicite a largura e altura de um retângulo e calcule sua área

"""
#Solicitamos o valor da largura da area a ser calculada.
largura = float(input("Qual a largura do seu retângulo: "))

#Solicitamos o valor da altura da area a ser calculada.
altura = float(input("Qual a altura do seu retângulo: "))

#Calculamos a area e armazenamos o valor na variavel area
area = altura * largura

#Imprimimos na tela do usuário a frase abaixo informando sua largura, altura e area
print(f"O seu retângulo tem de L:{largura} e A:{altura} possuindo uma área de {area}")