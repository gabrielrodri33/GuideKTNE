import os

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
        2: {'vermelho': '\033[31m', 'limpa': '\033[0m'}
    }

    if option == 1:
        mensagem = f'{cores[1]["verde"]}Corta!{cores[1]["limpa"]}'
    
    else:
        mensagem = f'{cores[2]["vermelho"]}Não Corta!{cores[2]["limpa"]}'

    return print(mensagem)

def validation(option):
    status = False
    match option:
        case 1:
            while not status:
                try:
                    
                    option = input("Contém entrada paralela? [S/N] ").upper().strip()
                    
                    if option and option[0] in ["S", "N"]:
                        status = True

                    else:
                        separador("Entrada inválida!", 7)
                        print('Digite "S" ou "N"')
                        separador(20, 1)
                
                except ValueError as e:
                    print(f"Error: {e}")
        
        case 2:
            while not status:
                try:
                    
                    option = input("Contém 2 ou mais pilhas? [S/N] ").upper().strip()
                    
                    if option and option[0] in ["S", "N"]:
                        status = True

                    else:
                        separador("Entrada inválida!", 7)
                        print('Digite "S" ou "N"')
                        separador(20, 1)
                
                except ValueError as e:
                    print(f"Error: {e}")
        
        case 3:
            while not status:
                try:
                    
                    option = input("O último dígito é par? [S/N] ").upper().strip()
                    
                    if option and option[0] in ["S", "N"]:
                        status = True

                    else:
                        separador("Entrada inválida!", 7)
                        print('Digite "S" ou "N"')
                        separador(20, 1)
                
                except ValueError as e:
                    print(f"Error: {e}")
    
    return option

def primary_lists():
    clear_console()
    separador(20, 1)

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

'''
Vermelho OK
Vermelho - Led OK
Vermelho - Estrela OK
Vermelho - Led - Estrela OK
Vermelho - Azul OK
Vermelho - Azul - Led OK
Vermelho - Azul - Led - Estrela OK

Azul OK
Azul - Led OK
Azul - Estrela OK
Azul - Estrela - Led OK

Led OK
Estrela OK
Led - Estrela OK
'''

def secondary_lists(red, blue, star, led):
    no_cut = cut = 0

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

    for i in red_star:
        if i == "N":
            no_cut += 1
        
        elif i in {"C", "S", "P", "B"}:
            cut += 1

    if no_cut > cut:
        answer(2)

    elif no_cut == cut: 
        answer(2)

    else:
        answer(1)

def principal():
    count = 0

    red, blue, star, led = primary_lists()

    secondary_lists(red, blue, star, led)

    # print(red)
    # print(blue)
    # print(star)
    # print(led)

#Programa principal
principal()