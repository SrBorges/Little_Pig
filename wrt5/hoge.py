import random

def hoge(serie, personagem):
    print(serie + personagem)
    list = [serie, personagem]
    len = 9
    all = "".join(random.sample(list[0] + list[1], len))
    for x in all:
        all = "".join(random.sample(list[0] + list[1], len))
        print(all)

def hogeU(serie, personagem):
    list = [serie, personagem]
    len = 9
    all = "".join(random.sample(list[0] + list[1], len))
    for x in all:
        all = "".join(random.sample(list[0] + list[1], len))
        print(all)


