import statistics
import math
import funcoes_simples

def simetrias(q1,q2,q3):

    tipo = ['Assimetria Positiva / a direita','Assimetria Negativa / a esquerda','Simetrico']

    if(q2 - q1) < (q3 - q2):
        return tipo[0]
    elif(q2 - q1) > (q3 - q2):
        return tipo[1]
    elif(q2 - q1) == (q3 - q2):
        return tipo[2]
    else:
        print('ERROR')
        return None

def limites(q1,q3,intervalo):

    inf = q1 - (1.5 * intervalo)
    sup = q3 + (1.5 * intervalo)

    return inf,sup

def coeficiente_de_bowley(q1,q2,q3):

    b = ((q3 - q2) - (q2 - q1)) / (q3 - q1)

    return b

def intervalo_interquartil(quartil1,quartil3):
    interv = (quartil3 - quartil1)
    return interv

def dividir_intervalos(numeros):
    numeros.sort()  #CHUPA DANTE
    mediana = statistics.median(numeros)
    tam = len(numeros)

    index_med = math.floor(tam / 2)

    quartil1 = statistics.median(numeros[:index_med])

    if tam % 2 == 0:
        quartil3 = statistics.median(numeros[index_med:])
    else:
        quartil3 = statistics.median(numeros[index_med+1:])

    return quartil1,mediana,quartil3

def coeficiente_de_assimetria(media,lista,dp):

    if len(lista) == 1:
        moda = lista[0]
        return (media - moda) / dp
    else:
        return 'nao e possivel calcular o coef de assimetria'

def print_organizado(q1,q2,q3,intervalo,msg,e,b,inf,sup):

    print(f"Quartil1: {q1}\nQuartil2: {q2}\nQuartil3: {q3}\nIntervalo interquartil: {intervalo}\nTipo de simetria dos quartis: {msg}\nCoeficiente de assimetria: %.4f " %e,
          f"\nCoeficiente de Bowley: %.4f\nLimite inferior: {inf}\nLimite superior: {sup}" %b)
    return None

def processos(numeros):

    q1,q2,q3 = dividir_intervalos(numeros)
    intervalo = intervalo_interquartil(q1,q3)
    msg = simetrias(q1,q2,q3)
    b = coeficiente_de_bowley(q1,q2,q3)
    inf, sup = limites(q1,q3,intervalo)

    moda = statistics.multimode(numeros)
    media = statistics.mean(numeros)
    var = funcoes_simples.variancia(numeros,media)
    dp = funcoes_simples.desvio_padrao(var)
    e = coeficiente_de_assimetria(media,moda,dp)

    print_organizado(q1, q2, q3, intervalo,msg,e,b,inf,sup)

    return None