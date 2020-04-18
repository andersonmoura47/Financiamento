#coding: utf-8:
"""
Comentários:
    Este modulo apresenta funções para calculo das parcelas e valor futuro de acordo com sistema de amortização desejado:
        Sistema de Amortização Constante (SAC)
        Sistema Francês de Amortização (PRICE)
        Sistema de Amortização Americano (SAA)

    Nas linhas finais do codigo as funções são chamadas e executadas. Para simular e conferir os valores obtidos:
        https://fazaconta.com/financiamentos-tabela-sac.htm
    
    Contatos:
        Guithub: Anderson Moura - andersonmoura47
        Instagram: anderson_moura47

"""
#~~~~~~~~~~~~~~~~~~~~~~~~~~> CONVERSÃO DE TAXA <~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def conversao_de_taxa(i, converter_taxa):
    if converter_taxa == 1: #converter de a.a para a.m:
        i = ((1 + i) ** (1/12)) - 1
    elif converter_taxa == 2: #converter de a.m para a.a formula:
        i = ((1 + i) ** 12) - 1
    return i

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~> SAC <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def sac(pv, i, n, converter_taxa = 0):
    """
    Calcula um financiamento no sistema SAC, e retorna a lista com os valores das parcelas
    Argumentos:
        pv: recebe o valor presente do financiamento
        i: recebe a taxa (lembrando que a taxa deve estar no mesmo periodo temporal que as parcelas)
        n: numero de parcelas (EX: numero de meses)
    Para converter a taxa de ao ano para ao mês mude o valor da variável "converter_taxa" para 1
    Para converter a taxa de ao mês para ao ano mude o valor da variável "converter_taxa" para 2
    """
    i = i / 100
    i = conversao_de_taxa(i, converter_taxa)
    si = pv
    am = pv / n # constante
    s = 0
    parc = []
    for a in range(n):
        j = si * i
        pmt = am + j
        sd = si - am
        s += pmt
        si = sd
        parc.append(float('%.2f' %pmt))
    return (parc)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~> PRICE <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def price(pv, i, n, converter_taxa = 0):
    """
    Calcula um financiamento no sistema PRICE, e retorna a lista com os valores das parcelas
    Argumentos:
        pv: recebe o valor presente do financiamento
        i: recebe a taxa (lembrando que a taxa deve estar no mesmo periodo temporal que as parcelas)
        n: numero de parcelas (EX: numero de meses)
    Para converter a taxa de ao ano para ao mês mude o valor da variável "converter_taxa" para 1
    Para converter a taxa de ao mês para ao ano mude o valor da variável "converter_taxa" para 2
    """
    i = i / 100
    i = conversao_de_taxa(i, converter_taxa)
    si = pv
    pmt = pv * (i / (1 - ((1 + i)**(-n)))) # constante
    s = 0
    parc = []
    for a in range(n):
        j = si * i
        am = pmt - j
        sd = si - am
        s += pmt
        si = sd
        parc.append(float('%.2f' %pmt))
    return (parc)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~> SAA <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def saa(pv, i, n, converter_taxa = 0):
    """
    Calcula um financiamento no sistema SAA, e mostra os valores das parcelas a serem pagas e o valor total
    Argumentos:
        pv: recebe o valor presente do financiamento
        i: recebe a taxa (lembrando que a taxa deve estar no mesmo periodo temporal que as parcelas)
        n : numero de parcelas (EX: numero de meses)
    Para converter a taxa de ao ano para ao mês mude o valor da variável "converter_taxa" para 1
    Para converter a taxa de ao mês para ao ano mude o valor da variável "converter_taxa" para 2
    """
    i = i / 100
    i = conversao_de_taxa(i, converter_taxa)
    si = pv
    s = 0
    parc = []
    for a in range(n):
        j = si * i
        if (a + 1) != n: # AM = 0
            am = 0
        else:            # AM + SI
            am = si
        pmt = am + j
        sd = si - am
        s += pmt
        si = sd
        parc.append(float('%.2f' %pmt))
    return (parc)

"""
#==========================================CHAMANDO AS FUNÇÕES=======================================
pv = 100000
i = 8
n = 60
convert_tax = 1 #int(input("Deseja converter a taxa? \n0 - Não\n1 - De a.a para a.m\n2 - De a.m para a.a\nDigite o número desejado:"))
# 0 - não | 1 - de a.a -> a.m | 2 - a.m -> a.a

a = sac(pv, i, n, converter_taxa = convert_tax)
b = price(pv, i, n, converter_taxa = convert_tax)
c = saa(pv, i, n, converter_taxa = convert_tax)

print('Valor: R$',pv, '\nTaxa: ',i,'%', '\nParcelas: ', n)
print('\nSAC:\n Parcelas: ', a, '\n Valor total: ', sum(a))
print('\nPRICE:\n Parcelas: ', b, '\n Valor total: ', sum(b))
print('\nSAA:\n Parcelas: ', c, '\n Valor total: ', sum(c))
"""

'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~> Anotações - formas de calculo: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- TABELA: n|Saldo i (Si)|juros (j)|Amortização (AM)|    Parcela (PMT)     |    Saldo f (SD)
- SAC:     |  SD n-1    | Si * i  |     PV / n     |         AM + j       | Si - AM      #AM CONSTANTE
- PRICE:   |  SD n-1    | Si * i  |     PMT-j      |(PV(i/(1-((1+i)*-n))))| Si - AM      #PMT CONSTANTE
- SAA:     |  SD n-1    | Si * i  |   0,0...Si     |         AM + j       | Si - AM
# SAC - AM CONSTANTE, PMT = AM + J
# PRICE - PMT CONSTANTE, AM = PMT - J
# SAA - PAGA JUROS CONSTANTE, PV PAGO NA ULTIMA PMT, AM = 0, NA ULTIMA PMT: AM + SI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

'''
