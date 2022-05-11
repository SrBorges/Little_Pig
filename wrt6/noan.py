import random

def noan(nome, ano):
    print(nome + ano)
    list = [nome, ano]
    len = 9
    all = "".join(random.sample(list[0] + list[1] + "*", len))
    for x in all:
        all = "".join(random.sample(list[0] + list[1] + "*", len))
        print(all)

def noanU(nome, ano):
    list = [nome, ano]
    len = 9
    all = "".join(random.sample(list[0] + list[1] + "*", len))
    for x in all:
        all = "".join(random.sample(list[0] + list[1] + "*", len))
        print(all)
