def primary_lists():
    red = ["S", "C", "S", "P", "S", "N", "B", "B"]
    blue = ["S", "P", "S", "S", "P", "N", "N", "P"]
    star = ["C", "C", "N", "P", "P", "N", "B", "B"]
    led = ["P", "N", "S", "B", "N", "B", "P", "B"]

    parallel = input("Contém entrada paralela? [S/N] ").upper().strip()
    battery = input("Contém 2 ou mais pilhas? [S/N] ").upper().strip()
    digit = input("O último dígito é par? [S/N] ").upper().strip()

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
        print("Não corta!")

    elif no_cut == cut: 
        print("Não corta!\nIGUAL!!!!")

    else:
        print("Corta!")

def principal():
    red, blue, star, led = primary_lists()
    secondary_lists(red, blue, star, led)

    # print(red)
    # print(blue)
    # print(star)
    # print(led)

#Programa principal
principal()