def listas():
    vermelho = ["S", "C", "S", "P", "S", "N", "B", "B"]
    azul = ["S", "P", "S", "S", "P", "N", "N", "P"]
    estrela = ["C", "C", "N", "P", "P", "N", "B", "B"]
    led = ["P", "N", "S", "B", "N", "B", "P", "B"]

    paralela = input("Contém entrada paralela? [S/N] ").upper().strip()
    pilhas = input("Contém 2 ou mais pilhas? [S/N] ").upper().strip()
    digito = input("O último dígito é par? [S/N] ").upper().strip()

    if paralela[0] == "N":
        vermelho = ['X' if x == 'P' else x for x in vermelho]
        azul = ['X' if x == 'P' else x for x in azul]
        estrela = ['X' if x == 'P' else x for x in estrela]
        led = ['X' if x == 'P' else x for x in led]

    if pilhas[0] == "N":
        vermelho = ['X' if x == 'B' else x for x in vermelho]
        azul = ['X' if x == 'B' else x for x in azul]
        estrela = ['X' if x == 'B' else x for x in estrela]
        led = ['X' if x == 'B' else x for x in led]

    if digito[0] == "N":
        vermelho = ['X' if x == 'S' else x for x in vermelho]
        azul = ['X' if x == 'S' else x for x in azul]
        estrela = ['X' if x == 'S' else x for x in estrela]
        led = ['X' if x == 'S' else x for x in led]


    return vermelho, azul, estrela, led

def principal():
    vermelho, azul, estrela, led = listas()

    print(vermelho)
    print(azul)
    print(estrela)
    print(led)

#Programa principal
principal()