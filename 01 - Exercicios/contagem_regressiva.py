"""
Contagem regressiva: Peça um número inteiro positivo e use um loop while para exibir uma contagem regressiva até 0.

"""

n = int(input("Digite um número: "))


if(n >= 0):
    while(n > 0):
        n -= 1
        print(n)
else:
    print("Digite apenas números positivos.")
      