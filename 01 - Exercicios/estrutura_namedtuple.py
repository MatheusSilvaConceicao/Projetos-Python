#Crie um tipo Pessoa com nome, idade e cidade. Crie 3 objetos e mostre os dados.

from collections import namedtuple

pessoa = namedtuple("pessoa",["nome","idade","cidade"])

pessoa1 = pessoa(nome="Marcos",idade=45,cidade="Santos")
pessoa2 = pessoa(nome="Adriana",idade=39,cidade="São Vicente")
pessoa3 = pessoa(nome="Mikaelly",idade=10,cidade="São Vicente")

print(pessoa1)
print(pessoa2)
print(pessoa3)