import diagrama
import words
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def separador(option):
    if option == 1:
        print('\033[36m', "-="*25, "\033[0m")
    else:
        print('\033[31m', "Entrada inválida!", "\033[0m")

def center_text(texto, n):
    largura = n
    texto_formatado = texto.center(largura)

    return print(texto_formatado)

def validation():
    status = False
    while not status:
        try:
            clear_console()
            separador(1)
            center_text("Menu Principal", 50)
            separador(1)
            option = int(input("1- Diagrama de Venn\n2- Senha\n3- Sair\n"))

            if 1 <= option <=3:
                status = True
            
            else:
                clear_console()
                separador(1)
                separador(2)
                print("Escolha uma opção de 1 a 3!")

        except ValueError:
                clear_console()
                separador(30, 1)
                separador(2)
                print("Por favor insira um número")
    
    return option

def execute():
    option = 0
    separador(1)

    while option != 3:
        option = validation()
        if option == 1:
            diagrama.principal()

        elif option == 2:
            words.principal()

    print("Obrigado! Volte sempre!")

execute()