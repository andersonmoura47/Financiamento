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
#~~~~~~~~~~~~~~~~~~~~~~~~~~> SELECIONA SISTEMA <~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def seleciona_sistema():
    q = True
    while q == True:
        sist = int(input('\nQual sistema deseja utilizar?\n1 - SAC\n2 - PRICE\n3 - SAA\n'))
        if sist == 1:
            a = sac(pv, i, n)
            q = False
        elif sist == 2:
            a = price(pv, i, n)
            q = False
        elif sist == 3:
            a = saa(pv, i, n)
            q = False
        else:
            q = False
    return a

#~~~~~~~~~~~~~~~~~~~~~~~~~~> CONVERSÃO DE TAXA <~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def conversao_de_taxa(i):
    v = True
    while v == True: 
        p = int(input('\nDeseja converter a taxa?\n1 - Sim\n2 - Não\n'))
        if p == 1:
            v2 = True
            while v2 == True: 
                p2 = int(input('\nEscolha a opção de conversão desejada: \n1 - Anual para mensal \n2 - Mensal para Anual\n'))
                if p2 == 1:
                    i = (((1 + (i/100)) ** (1/12)) - 1) * 100 # conversao de a.a para a.m
                    v2 = False # sair da p2
                elif p2 == 2:
                    i = (((1 + (i/100)) ** 12) - 1) * 100    # conversao de a.m para a.a
                    v2 = False # sair da p2
                else:
                    print('Opção inválida!')
            v = False # sair da p1
        elif p == 2:
            i = i # mantem a taxa
            v = False # sair da p1
        else:
            print('Opção inválida!')
    return i

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~> SAC <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def sac(pv, i, n):
    """
    Calcula um financiamento no sistema SAC, e retorna a lista com os valores das parcelas
    Argumentos:
        pv: recebe o valor presente do financiamento
        i: recebe a taxa (lembrando que a taxa deve estar no mesmo periodo temporal que as parcelas)
        n: numero de parcelas (EX: numero de meses)
    """
    i = conversao_de_taxa(i)
    i = i / 100
    si = pv # saldo inicial (si) começa como valor presente (PV)
    am = pv / n # amortização (am) constante
    parc = [] # lista para acumular o valor das parcelas
    for a in range(n):
        j = si * i # juros (j)
        pmt = am + j # parcelas (pmt)
        sd = si - am # saldo final (sd)
        si = sd # saldo inicial passa a ser o saldo final
        parc.append(float('%.2f' %pmt))
    return (parc)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~> PRICE <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def price(pv, i, n):
    """
    Calcula um financiamento no sistema PRICE, e retorna a lista com os valores das parcelas
    Argumentos:
        pv: recebe o valor presente do financiamento
        i: recebe a taxa (lembrando que a taxa deve estar no mesmo periodo temporal que as parcelas)
        n: numero de parcelas (EX: numero de meses)
    """
    i = conversao_de_taxa(i)
    i = i / 100
    si = pv
    pmt = pv * (i / (1 - ((1 + i)**(-n)))) # parcelas (pmt) constantes
    parc = []
    for a in range(n):
        j = si * i
        am = pmt - j
        sd = si - am
        si = sd
        parc.append(float('%.2f' %pmt))
    return (parc)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~> SAA <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def saa(pv, i, n):
    """
    Calcula um financiamento no sistema SAA, e mostra os valores das parcelas a serem pagas e o valor total
    Argumentos:
        pv: recebe o valor presente do financiamento
        i: recebe a taxa (lembrando que a taxa deve estar no mesmo periodo temporal que as parcelas)
        n : numero de parcelas (EX: numero de meses)
    """
    i = conversao_de_taxa(i)
    i = i / 100
    si = pv
    parc = []
    for a in range(n):
        j = si * i
        if (a + 1) != n: # a amortização só é somada ao saldo inicial no último pagamento
            am = 0
        else:            # AM + SI
            am = si
        pmt = am + j
        sd = si - am
        si = sd
        parc.append(float('%.2f' %pmt))
    return (parc)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~> CHAMANDO AS FUNÇÕES <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
pv = int(input('Digite o valor: '))
i = float(input('Digite a taxa: ')) # taxa mensal (7.95% a.a)
n = int(input('Digite o numero de periodos: '))

a = seleciona_sistema() # a retorna uma lista com as parcelas

print('\nValor das parcelas:')
for j in range(len(a)):
    print(j + 1,' - R$', a[j])
print('\nValor: R$', pv, '\nTaxa: ', i, '%', '\nParcelas: ', n)
print('\nValor total pago: R$', sum(a),'\n')

"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~> Anotações - formas de calculo: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- TABELA: n|Saldo i (Si)|juros (j)|Amortização (AM)|    Parcela (PMT)     |    Saldo f (SD)
- SAC:     |  SD n-1    | Si * i  |     PV / n     |         AM + j       | Si - AM      #AM CONSTANTE
- PRICE:   |  SD n-1    | Si * i  |     PMT-j      |(PV(i/(1-((1+i)*-n))))| Si - AM      #PMT CONSTANTE
- SAA:     |  SD n-1    | Si * i  |   0,0...Si     |         AM + j       | Si - AM
# SAC - AM CONSTANTE, PMT = AM + J
# PRICE - PMT CONSTANTE, AM = PMT - J
# SAA - PAGA JUROS CONSTANTE, PV PAGO NA ULTIMA PMT, AM = 0, NA ULTIMA PMT: AM + SI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
