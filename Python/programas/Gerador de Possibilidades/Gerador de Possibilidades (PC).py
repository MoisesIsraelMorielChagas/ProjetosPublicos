from time import sleep
from os import system


def clear():
    #system('clear')
    system('cls')


def linha():
    print('-'*42)


def CG():
    linha()
    print('Gerador de Possibilidades'.center(42))
    linha()


def geraLista(tamanho, default = ' '):
    lista = list()
    for x in range(tamanho):
        lista.append(default)
    return lista

    
def geraPossibilidades(variantes, nElementos, nPossibilidades):
    poss_Inicial = variantes[0]
    poss_Final = variantes[-1]
    elementos = geraLista(nElementos, poss_Inicial)
    nElementos -= 1
    contador = 0
    print(f'  Serão geradas {nPossibilidades} combinações:\n\n')
    sleep(2.4)
    for p in range(nPossibilidades):
        elementoTexto = contextualizarLista(elementos[:])
        contador+=1
        if (contador != 1) and (contador % 100 == 1):
            print('\n  Pressione qualquer tecla para continuar.\n')
            if input((' >>> ').lower()) == 'break':
                linha()
                print('SESSÃO FINALIZADA!'.center(42))
                linha()
                break
            print()
        print(f'  {contador:>10} => {elementoTexto}')
        if p == (nPossibilidades-1): break
        for cada in range(nElementos, -1, -1):
            e = elementos[cada]
            if e != poss_Final:
                indiceE = int(variantes.index(e))
                indiceSeguinte = indiceE + 1
                e = variantes[indiceSeguinte]
                elementos[cada] = e
                break
            else:
                e = poss_Inicial
                elementos[cada] = e
    
        
def contextualizarLista(lista):
    texto = ''
    for x in lista:
        texto += str(x)
    return texto
        

def ajeitarLista(lista):
    semRepeticao = list()
    while ' ' in lista:
        lista.remove(' ')
    for x in lista:
        if x not in semRepeticao: semRepeticao.append(x)
    return semRepeticao

        
def Principal(listaDeVariantes, numeroDeElementos):
    variantes = listaDeVariantes
    quantidadeDeVariantes = len(variantes)
    nElementos = numeroDeElementos
    nPossibilidades = quantidadeDeVariantes ** nElementos
    possibilidades = geraPossibilidades(variantes, nElementos, nPossibilidades)


def LeiaInt(txt):
    while True:
        try:
            num = int(input(txt))
        except:
            linha()
            print('__Valor_Inválido__'.center(42))
            linha()
            continue
        return num


while True:
    clear()
    CG()
    variantes = ajeitarLista(list(input('  Elementos possiveis: \n\n\t')))
    linha()
    numeroDeCasas = LeiaInt('  Numero de casas: \n\n\t')
    linha()
    if len(variantes) < 1 or numeroDeCasas < 1:
        print('Não há possibilidades!'.center(42))
        linha()
        sleep(3/2)
        continue
    clear()
    CG()
    Principal(variantes, numeroDeCasas)
    sleep(1/2)
    print('\n   Digite 1 para recomeçar\n  ou enter para sair...')
    sleep(1/2)
    destino = str(input('\n\n >>>'))
    if destino == '1':
        continue
    break
exit()

    
    
