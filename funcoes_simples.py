import statistics
import math

def min_max(numeros):
    return min(numeros),max(numeros)

def moda(numeros):
    modas = statistics.multimode(numeros)

    if len(numeros) == len(modas):
        print('Sem Moda')
    else:
        print("| ",end='')
        for i in range(len(modas)):
            print(modas[i],end=" | ")
        print()
    return None

def mediana(numeros):
    return statistics.median(numeros)

def media_simples(numeros):
    return statistics.mean(numeros)

def media_ponderada(numeros,pesos):
    soma = 0
    for i in range(len(numeros)):
        soma += numeros[i] * pesos[i]
    media = soma / sum(pesos)
    return media

def amplitude(numeros):
    return max(numeros) - min(numeros)

def desvio_medio_absoluto(numeros,media):
    soma = 0
    for i in numeros:
        soma += abs(i - media)

    return soma / len(numeros)

def variancia(numeros,media):
    soma = 0
    for i in range(len(numeros)):
        soma += (abs(numeros[i] - media) ** 2)
    return soma/len(numeros)

def desvio_padrao(var):
    dp = var
    return math.sqrt(dp)

def coeficiente_de_variacao(dp,med):
    cv = dp / med
    return cv*100

def escore_padronizado(numeros,media,desvio_padrao):
    escores = []
    for i in range(len(numeros)):
        escores.append((numeros[i] - media) / desvio_padrao)

    print("| ",end='')
    for val in escores:
        print("%.4f" %val,end=' | ')
    print()

    return None

def simetrias(lista,media):

    if len(lista) == 1:
        moda = lista[0]

        tipo = ['assimetrica a direita / assimetria positiva','assimetrica a esquerda / assimetria negativa','Simetrico']

        if media > moda:
            return tipo[0]
        elif moda > media:
            return tipo[1]
        elif media == moda:
            return tipo[2]
    else:
        return 'Nao e possivel calcular'

def processos(numeros):

    print('tem media ponderada ?')
    resposta = input()
    if resposta.lower() == 'sim' or resposta.lower() == 's' or resposta.lower() == 'ok':
        print('quais sao os pesos ?')
        pesos = list(map(int,input().split()))

        print('Media ponderada: ',media_ponderada(numeros,pesos))

    mediasimples = media_simples(numeros)
    variancia_prt = variancia(numeros,mediasimples)
    desviopadrao = desvio_padrao(variancia_prt)

    menor,maior = min_max(numeros)
    print('Valor minimo:',menor)
    print('Valor maximo:',maior)
    print('Media simples: %.4f' %mediasimples)
    print('Moda(s): ',end='')
    moda(numeros)
    print('Mediana: ',mediana(numeros))
    print('Amplitude: ',amplitude(numeros))
    print('DMA: %.4f' %desvio_medio_absoluto(numeros,mediasimples))
    print('Variancia: %.4f' %variancia_prt)
    print('Desvio padrao: %.4f' %desviopadrao)
    print('Coeficiente de variacao: %.4f'%coeficiente_de_variacao(desviopadrao,mediasimples),'%')
    print('Escore padronizado para essa sequencia: ')
    print('Simetria:', simetrias(statistics.multimode(numeros), mediasimples))
    escore_padronizado(numeros,mediasimples,desviopadrao)

    return None