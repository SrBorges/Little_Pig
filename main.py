# -*- coding:UTF-8 -*-
from wrt1 import nmid
from wrt2 import nmam
from wrt3 import emdi
from wrt4 import anid
from wrt5 import hoge
from wrt6 import noan


print("1 - Nome + idade. \n")
print("2 - Nome + Companheiro(a) + dia. \n")
print("3 - Empresa + dia. \n")
print("4 - Aniversário + idade. \n")
print("5 - Filme/Série + Personagem. \n")
print("6 - Nome + Ano de nascimento. \n")
print("9 - Sair. \n")


operador = int(input("Informe o operador: "))
opc = [1, 2, 3, 4, 5, 6, 9]

if operador == 1:
    nome = str(input("Digite seu nome: "))
    idade = str(input("Digite sua idade: "))
    nmid.nmid(nome, idade)
    nmid.nmidU(nome.upper(), idade.upper())
elif operador == 2:
    nome = str(input("Informe seu nome: "))
    comp = str(input("Infome o nome do companheiro(a): "))
    dia = str(input("Informe o dia: "))
    nmam.nmam(nome, comp, dia)
    nmam.nmamU(nome.upper(), comp.upper(), dia)
elif operador == 3:
    empresa = str(input("Informe a empresa: "))
    dia = str(input("Informe um dia: "))
    emdi.emdi(empresa, dia)
    emdi.emdiU(empresa.upper(), dia)
elif operador == 4:
    aniversario = str(input("Informe o aniversário: "))
    idade = str(input("Informe a idade: "))
    anid.anid(aniversario, idade)
elif operador == 5:
    serie = str(input("Série ou filme: "))
    personagem = str(input("Personagem: "))
    hoge.hoge(serie, personagem)
    hoge.hogeU(serie.upper(), personagem.upper())
elif operador == 6:
    nome = str(input("Informe o nome: "))
    ano = str(input("Informe o ano de nascimento: "))
    noan.noan(nome, ano)
    noan.noanU(nome.upper(), ano)
elif operador == 9:
    print("Gerador finalizado. \n")
    print("Até a próxima. :) \n")


while operador not in opc:
    print("Valor inválido. ")
    operador = int(input("Informe o operador: "))

    if operador == 1:
        nome = str(input("Digite seu nome: "))
        idade = str(input("Digite sua idade: "))
        nmid.nmid(nome, idade)
        nmid.nmidU(nome.upper(), idade.upper())
    elif operador == 2:
        nome = str(input("Informe seu nome: "))
        comp = str(input("Infome o nome do companheiro(a): "))
        dia = str(input("Informe o dia: "))
        nmam.nmam(nome, comp, dia)
        nmam.nmamU(nome.upper(), comp.upper(), dia)
    elif operador == 3:
        empresa = str(input("Informe a empresa: "))
        dia = str(input("Informe um dia: "))
        emdi.emdi(empresa, dia)
        emdi.emdiU(empresa.upper(), dia)
    elif operador == 4:
        aniversario = str(input("Informe o aniversário: "))
        idade = str(input("Informe a idade: "))
        anid.anid(aniversario, idade)
    elif operador == 5:
        serie = str(input("Série ou filme: "))
        personagem = str(input("Personagem: "))
        hoge.hoge(serie, personagem)
        hoge.hogeU(serie.upper(), personagem.upper())
    elif operador == 6:
        nome = str(input("Informe o nome: "))
        ano = str(input("Informe o ano de nascimento: "))
        noan.noan(nome, ano)
        noan.noanU(nome.upper(), ano)
    elif operador == 9:
        print("Gerador finalizado. \n")
        print("Até a próxima. :) \n")
