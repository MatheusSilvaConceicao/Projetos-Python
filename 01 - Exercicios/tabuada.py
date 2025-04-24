#Gere a tabuada de um número

num = int(input("Você quer a tabuada de qual número: "))
i = 0

while i < 10:
    print(f"{num} x {i} = {num*i}")
    i += 1