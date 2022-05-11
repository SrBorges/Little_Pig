import random

def anid(aniversario, idade):
    print(aniversario + idade)
    len = 9
    list = [aniversario, idade]
    print(aniversario + idade)
    all = "" .join(random.sample(list[0] + list[1] + "*", len))
    for x in all:
        all = "".join(random.sample(aniversario + idade + "*", len))
        print(all)




