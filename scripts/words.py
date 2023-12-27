from itertools import product
import os
import time

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def separador(n, cor):
    cores = {
        1: {'azul': '\033[36m', 'limpa' : '\033[0m'},
        2: {'verde': '\033[32m', 'limpa' : '\033[0m'},
        3: {'roxo' : '\033[95m' , 'limpa' : '\033[0m'},
        4: {'amarelo': '\033[33m', 'limpa': '\033[0m'},
        5: {'vermelho': '\033[31m', 'limpa': '\033[0m'}
    }

    if cor == 1:
        mensagem = f'{cores[1]["azul"]}-={cores[1]["limpa"]}' * n

    elif cor == 2:
        mensagem = f'{cores[2]["verde"]}-={cores[2]["limpa"]}' * n

    elif cor == 3:
        mensagem = f'{cores[3]["roxo"]}-={cores[3]["limpa"]}' * n

    elif cor == 5:
        mensagem = f'{cores[5]["vermelho"]}-={cores[5]["limpa"]}' * n

    elif cor == 6:
        mensagem = f'{cores[4]["amarelo"]}-={cores[4]["limpa"]}' * n
    
    elif cor == 7:
        mensagem = f'{cores[5]["vermelho"]}{n}{cores[5]["limpa"]}'
    return print(mensagem)

def lista_palavras():
    lista = ["acessa", "ajuda", "amigo", "antes", "arcos", "baile", "balas", "bispo", "chefe", "cheio", "cinto", "cravo", "etapa", "etnia", "flora", "lazer", "legal", "lugar", "parte", "parto", "perto", "porta", "regra", "resto", "salve", "sente", "setor", "sexta", "tecla", "tinta", "torta", "touro", "trato", "valer", "veado"]

    return lista

def letra(n, position):
    possivel_letra = []
    lista = lista_palavras()

    letra_lista = [palavra[n] for palavra in lista]

    clear_console()
    separador(14, 1)
    primeira = input(f"{position}ª Letra: ").strip().lower()

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
    primeira_letra = letra(0, 1)
    segunda_letra = letra(1, 2)
    terceira_letra = letra(2, 3)
    quarta_letra = letra(3, 4)
    quinta_letra = letra(4, 5)
    descobrir_palavra(primeira_letra, segunda_letra, terceira_letra, quarta_letra, quinta_letra)
    

def descobrir_palavra(primeira_letra, segunda_letra, terceira_letra, quarta_letra, quinta_letra):
    lista = lista_palavras()
    listas = [primeira_letra, segunda_letra, terceira_letra, quarta_letra, quinta_letra]

    combinacoes = list(product(*listas))

    palavras = [''.join(comb) for comb in combinacoes]

    set_lista = set(lista)
    set_palavras = set(palavras)    

    palavras_em_comum = list(set_lista.intersection(set_palavras))

    for c in palavras_em_comum:
        print(c)
    
    time.sleep(5)
