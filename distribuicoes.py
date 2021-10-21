import statistics
def criar_intervalos(min, max, tam_itv):

    razao = (max - min) / tam_itv
    intervalos = []

    piso = float(min)
    for i in range(tam_itv):
        temp = [0] * 2
        temp[0], temp[1] = piso, piso + razao
        intervalos.append(temp)

        piso += razao

    return intervalos

def frequencia_simples_absoluta(valores,intervalos):

    lista_freq_abs = []

    for i in range(len(intervalos)):
        freq = 0
        for x in valores:
            if x >= intervalos[i][0] and x < intervalos[i][1]:
                freq += 1
        lista_freq_abs.append(freq)

    return lista_freq_abs

def frequencia_simples_relativa(lista_frequencia):

    total = sum(lista_frequencia)
    lista_freq_relativa = []

    for i in range(len(lista_frequencia)):
        lista_freq_relativa.append(lista_frequencia[i] / total)

    return lista_freq_relativa

def frequencia_acumulada_absoluta(valores,intervalos):

    lista_freq_absoluta = []

    for i in range(len(intervalos)):
        freq = 0
        for x in valores:
            if x < intervalos[i][1]:
                freq += 1
        lista_freq_absoluta.append(freq)

    return lista_freq_absoluta

def frequencia_acumulada_relativa(lista_frequencia):

    lista_freq_relativa = []

    tam = len(lista_frequencia)

    for i in range(tam):
        lista_freq_relativa.append(lista_frequencia[i] / lista_frequencia[tam-1])

    return lista_freq_relativa

def media(intervalo,freq_smp_abs):

    intervalos_medios = []

    for i in range(len(intervalo)):
        intervalos_medios.append((intervalo[i][0] + intervalo[i][1]) / 2)
        intervalos_medios[i] = intervalos_medios[i] * freq_smp_abs[i]

    media = sum(intervalos_medios) / sum(freq_smp_abs)

    print('Media: %.4f' %media)
    return None

def moda(intervalo,freq_smp_abs):
    intervalos_medios = []
    tam = len(intervalo)

    for i in range(tam):
        intervalos_medios.append((intervalo[i][0] + intervalo[i][1]) / 2)

    posicoes = []
    maximo = max(freq_smp_abs)

    for i in range(tam):
        if freq_smp_abs[i] == maximo:
            posicoes.append(intervalos_medios[i])

    print('Moda: ',posicoes)
    return None

def print_organizado(intervalos,freq_smp_abs,fre_smp_rel,freq_acm_abs,freq_acm_rel):

    for i in range(len(freq_acm_rel)):
        freq_acm_rel[i] *= 100
        fre_smp_rel[i] *= 100

    msg = ["Frequencia Simples","Frequencia Acumulada","Absoluta","Relativa %"]

    print(f"{msg[0]:^80} {msg[1]:^20}")
    print(f"{msg[2]:>30} {msg[3]:>20}{msg[2]:>30} {msg[3]:>20}")

    for i in range(len(intervalos)):
        print(f"{'[%.3f' %intervalos[i][0]} {'%.3f)'  %intervalos[i][1] : ^14}"
              f"{freq_smp_abs[i]:>4} {'%.3f' %fre_smp_rel[i]: >20} {freq_acm_abs[i]: >22} {'%.3f' %freq_acm_rel[i] : >23}")

    x,y = sum(freq_smp_abs),sum(fre_smp_rel)
    print("TOTAL: ",' '*15,x,'\t'*4,"%.2f" %y)

    return None

def processos(numeros):
    x = int(input('Em quantos intervalos partir ?\n'))
    y = float(input('Qual o limite maximo do conjunto ?\n'))
    #x,y = 5,1605

    if y < max(numeros):
        return None

    intervalos = criar_intervalos(min(numeros), y, x)

    freq_smp_abs = frequencia_simples_absoluta(numeros, intervalos)
    freq_smp_rel = frequencia_simples_relativa(freq_smp_abs)

    freq_acm_abs = frequencia_acumulada_absoluta(numeros, intervalos)
    freq_acm_rel = frequencia_acumulada_relativa(freq_acm_abs)

    print_organizado(intervalos, freq_smp_abs, freq_smp_rel,freq_acm_abs,freq_acm_rel)

    print()
    media(intervalos,freq_smp_abs)
    moda(intervalos,freq_smp_abs)

    return None
#print(media([[3200,4021],[4021,4842],[4842,5663],[5663,6484],[6484,7305]],[4,2,2,3,4]))
#print(moda([[3200,4021],[4021,4842],[4842,5663],[5663,6484],[6484,7305]],[4,2,2,3,4]))
#luan = [500, 520, 520, 540, 600, 600, 600, 700, 700, 720, 720, 720, 740, 800, 800, 800, 800, 840, 840, 850, 850, 900, 900, 950, 1020, 1020, 1020, 1600, 1600, 1600]
#processos(luan)