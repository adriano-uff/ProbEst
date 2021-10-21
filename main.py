import funcoes_simples
import distribuicoes
import quartis

def main():

    print('O QUE QUE TU QUER MONSTRAO ?')
    modo = int(input('[1] funcoes simples\n[2] distribuicao de frequencias\n[3] quartis\n'))

    if not modo == 1 and not modo == 2 and not modo == 3:
        print('Entrada invalida\nPrograma abortado')
        return None

    print('Entre com os valores, separados com um espaço: ')
    objeto = input().split()
    try:
        numeros = list(map(int,objeto))
    except ValueError:
        numeros = list(map(float,objeto))

    print('Esses sao os valores obtidos, deseja continuar ? [S/N]')
    print(numeros)
    print('Foram captados',len(numeros),'valores')

    opcao = input()
    if opcao.lower() == 'sim' or opcao.lower() == 's':
        if modo == 1:
            funcoes_simples.processos(numeros)
        if modo == 2:
            distribuicoes.processos(numeros)
        if modo == 3:
            quartis.processos(numeros)
    else:
        print("Programa abortado")
        return None
    return None

if __name__ == '__main__':
    main()