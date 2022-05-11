import random


def nmid(nome, idade):
    print(nome + idade)
    len = 9
    list = [nome, idade]
    print(nome + idade)
    all = "" .join(random.sample(list[0] + list[1], len))
    for x in all:
        all = "".join(random.sample(list[0] + list[1] + "@", len))
        print(all)

def nmidU(nome, idade):
    len = 9
    list = [nome, idade]
    all = "" .join(random.sample(list[0] + list[1], len))
    for x in all:
        all = "".join(random.sample(list[0] + list[1] + "@", len))
        print(all)






