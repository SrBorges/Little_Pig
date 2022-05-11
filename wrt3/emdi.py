import random

def emdi(empresa, dia):
    len = 9
    list = [empresa, dia]
    print(empresa + dia)
    all = "".join(random.sample(list[0] + list[1], len))
    for x in all:
        all = "".join(random.sample(list[0] + list[1], len))
        print(all)

def emdiU(empresa, dia):
    len = 9
    list = [empresa, dia]
    all = "".join(random.sample(list[0] + list[1], len))
    for x in all:
        all = "".join(random.sample(list[0] + list[1], len))
        print(all)