import random

def nmam(nome, comp, dia):
    print(nome + comp + dia)
    len = 9
    list = [nome, comp, dia]
    print(nome + comp + dia)
    all = "" .join(random.sample(list[0] + list[1] + list[2], len))
    for x in all:
        all = "".join(random.sample(list[0] + list[1] + list[2], len))
        print(all)

def nmamU(nome, comp, dia):
    len = 9
    list = [nome, comp, dia]
    all = "" .join(random.sample(list[0] + list[1] + list[2], len))
    for x in all:
        all = "".join(random.sample(list[0] + list[1] + list[2], len))
        print(all)
