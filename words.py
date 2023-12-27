from itertools import product

def lista_palavras():
    lista = ["acessa", "ajuda", "amigo", "antes", "arcos", "baile", "balas", "bispo", "chefe", "cheio", "cinto", "cravo", "etapa", "etnia", "flora", "lazer", "legal", "lugar", "parte", "parto", "perto", "porta", "regra", "resto", "salve", "sente", "setor", "sexta", "tecla", "tinta", "torta", "touro", "trato", "valer", "veado"]

    return lista

def letra(n):
    possivel_letra = []
    lista = lista_palavras()

    letra_lista = [palavra[n] for palavra in lista]

    primeira = input(" Letra: ").strip().lower()

    l1 = primeira[0]
    l2 = primeira[1]
    l3 = primeira[2]
    l4 = primeira[3]
    l5 = primeira[4]
    l6 = primeira[5]

    if l1 in letra_lista:
        possivel_letra.append(l1)

    if l2 in letra_lista:
        possivel_letra.append(l2)

    if l3 in letra_lista:
        possivel_letra.append(l3)

    if l4 in letra_lista:
        possivel_letra.append(l4)

    if l5 in letra_lista:
        possivel_letra.append(l5)

    if l6 in letra_lista:
        possivel_letra.append(l6)

    return possivel_letra

def principal():
    print("1° ", end="")
    primeira_letra = letra(0)
    print("2° ", end="")
    segunda_letra = letra(1)
    print("3° ", end="")
    terceira_letra = letra(2)
    print("4° ", end="")
    quarta_letra = letra(3)
    print("5° ", end="")
    quinta_letra = letra(4)
    descobrir_palavra(primeira_letra, segunda_letra, terceira_letra, quarta_letra, quinta_letra)
    

def descobrir_palavra(primeira_letra, segunda_letra, terceira_letra, quarta_letra, quinta_letra):
    lista = lista_palavras()
    listas = [primeira_letra, segunda_letra, terceira_letra, quarta_letra, quinta_letra]

    combinacoes = list(product(*listas))

    palavras = [''.join(comb) for comb in combinacoes]

    set_lista = set(lista)
    set_palavras = set(palavras)    

    palavras_em_comum = list(set_lista.intersection(set_palavras))

    print(palavras_em_comum)
#Programa principal
principal()
