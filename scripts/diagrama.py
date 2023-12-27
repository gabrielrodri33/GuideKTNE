import os
from itertools import permutations

'''
Vermelho / v OK
Vermelho - Led / vl OK
Vermelho - Estrela / ve OK
Vermelho - Led - Estrela / vle OK
Vermelho - Azul / va OK
Vermelho - Azul - Led / val OK
Vermelho - Azul - Led - Estrela / vale 

Azul / a OK
Azul - Led / al OK
Azul - Estrela / ae OK
Azul - Estrela - Led / ael OK

Led / l OK
Estrela / e OK
Led - Estrela / le OK
'''

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

def answer(option):
    cores = {
        1: {'verde': '\033[32m', 'limpa' : '\033[0m'},
        2: {'vermelho': '\033[31m', 'limpa': '\033[0m'},
        3: {'amarelo': '\033[33m', 'limpa': '\033[0m'}
    }

    if option == 1:
        mensagem = f'{cores[1]["verde"]}Corta!{cores[1]["limpa"]}'
    
    elif option == 2:
        mensagem = f'{cores[2]["vermelho"]}Não Corta!{cores[2]["limpa"]}'

    else:
        mensagem = f'{cores[3]["amarelo"]}Número Igual!{cores[3]["limpa"]}'

    return print(mensagem)

def validation(option):
    status = False
    match option:
        case 1:
            while not status:
                option = input("Contém entrada paralela? [S/N] ").upper().strip()
                
                if option and option[0] in ["S", "N"]:
                    status = True

                else:
                    separador("Entrada inválida!", 7)
                    print('Digite "S" ou "N"')
                    separador(28, 1)

        case 2:
            while not status:  
                    option = input("Contém 2 ou mais pilhas? [S/N] ").upper().strip()
                    
                    if option and option[0] in ["S", "N"]:
                        status = True

                    else:
                        separador("Entrada inválida!", 7)
                        print('Digite "S" ou "N"')
                        separador(28, 1)
            
        case 3:
            while not status: 
                    option = input("O último dígito é par? [S/N] ").upper().strip()
                    
                    if option and option[0] in ["S", "N"]:
                        status = True

                    else:
                        separador("Entrada inválida!", 7)
                        print('Digite "S" ou "N"')
                        separador(28, 1)
                
    return option

def primary_lists():
    clear_console()
    separador(28, 1)

    red = ["S", "C", "S", "P", "S", "N", "B", "B"]
    blue = ["S", "P", "S", "S", "P", "N", "N", "P"]
    star = ["C", "C", "N", "P", "P", "N", "B", "B"]
    led = ["P", "N", "S", "B", "N", "B", "P", "B"]

    parallel = validation(1)
    battery = validation(2)
    digit = validation(3)

    if parallel[0] == "N":
        red = ['X' if x == 'P' else x for x in red]
        blue = ['X' if x == 'P' else x for x in blue]
        star = ['X' if x == 'P' else x for x in star]
        led = ['X' if x == 'P' else x for x in led]

    if battery[0] == "N":
        red = ['X' if x == 'B' else x for x in red]
        blue = ['X' if x == 'B' else x for x in blue]
        star = ['X' if x == 'B' else x for x in star]
        led = ['X' if x == 'B' else x for x in led]

    if digit[0] == "N":
        red = ['X' if x == 'S' else x for x in red]
        blue = ['X' if x == 'S' else x for x in blue]
        star = ['X' if x == 'S' else x for x in star]
        led = ['X' if x == 'S' else x for x in led]

    return red, blue, star, led

def secondary_lists(red, blue, star, led):
    no_cut = cut = dynamic_list = 0

    word = search_word()

    if word == "S":
        return word

    dynamic_list, type_wire = dynamyc(red, blue, star, led, word)

    for i in dynamic_list:
        if i == "N":
            no_cut += 1
        
        elif i in {"C", "S", "P", "B"}:
            cut += 1

    if no_cut > cut:
        print(type_wire)
        answer(2)

    elif no_cut == cut: 
        print(type_wire)
        answer(3)

    else:
        print(type_wire)
        answer(1)

def search_word():
    words = ["V", "VL", "VE", "VLE", "VA", "VAL", "VALE", "A", "AL", "AE", "AEL", "L", "E", "LE", "S"]

    while True:
        separador(28, 1)
        wire = input("Especifique os fios apenas com as iniciais: ").strip().upper()

        permutations_list = [''.join(p) for p in permutations(wire)]

        possible_words = [p for p in permutations_list if p in words]

        if possible_words:
            word = possible_words[0]
            break

        else:
            separador("Fio não existe!", 7)
            print("Tente novamente!")

    return word

def dynamyc(red, blue, star, led, word):
    red_blue = [red[2], red[3], red[4], red[5]]
    red_star = [red[1], red[3], red[5], red[7]]
    red_led = [red[4], red[5], red[6], red[7]]
    red_blue_led = [red[4], red[5]]
    red_blue_star = [red[4], "N"]
    red_blue_star_led = ["N"]
    red_led_star = ["N", red[7]]

    blue_led = [blue[1], blue[3], blue[5], blue[7]]
    blue_star = [blue[4], blue[5], blue[6], blue[7]]
    blue_star_led = [blue[5], blue[7]]

    led_star = [led[4], led[5], led[6], led[7]]

    match word:
        case "V":
            return red, "Fio vermelho!"
        
        case "VL":
            return red_led, "Fio vermelho com led!"

        case "VE":
            return red_star, "Fio vermelho com estrela!"

        case "VLE":
            return red_led_star, "Fio vermelho com led e estrela!"

        case "VA":
            return red_blue, "Fio vermelho e azul!"

        case "VAL":
            return red_blue_led, "Fio vermelho com azul e led!"

        case "VALE":
            return red_blue_star_led, "Fio com tudo!"

        case "A":
            return blue, "Fio azul!"

        case "AL":
            return blue_led, "Fio azul com led!"

        case "AE":
            return blue_star, "Fio azul com estrela!"

        case "AEL":
            return blue_star_led, "Fio azul com estrela e led!"
        
        case "L":
            return led, "Fio branco com led!"
    
        case "E":
            return star, "Fio branco com estrela!"
        
        case "LE":
            return led_star, "Fio branco com estrela e led!"
        
        case _:
            return "S"

def principal():
    count = 0

    red, blue, star, led = primary_lists()
    while count != "S":
        count = secondary_lists(red, blue, star, led)
