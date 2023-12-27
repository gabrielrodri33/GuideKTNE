def listas():
    vermelho = ["S", "C", "S", "P", "S", "N", "B", "B"]
    azul = ["S", "P", "S", "S", "P", "N", "N", "P"]
    estrela = ["C", "C", "N", "P", "P", "N", "B", "B"]
    led = ["P", "N", "S", "B", "N", "B", "P", "B"]

    paralela = input("Contém entrada paralela? [S/N] ").upper().strip()
    pilhas = input("Contém 2 ou mais pilhas? [S/N] ").upper().strip()
    digito = input("O último dígito é par? [S/N] ").upper().strip()

    if paralela[0] == "N":
        vermelho = list(filter(lambda x: x != "P", vermelho))
        azul = list(filter(lambda x: x != "P", azul))
        estrela = list(filter(lambda x: x != "P", estrela))
        led = list(filter(lambda x: x != "P", led))

    if pilhas[0] == "N":
        vermelho = list(filter(lambda x: x != "B", vermelho))
        azul = list(filter(lambda x: x != "B", azul))
        estrela = list(filter(lambda x: x != "B", estrela))
        led = list(filter(lambda x: x != "B", led))

    if digito[0] == "N":
        vermelho = list(filter(lambda x: x != "S", vermelho))
        azul = list(filter(lambda x: x != "S", azul))
        estrela = list(filter(lambda x: x != "S", estrela))
        led = list(filter(lambda x: x != "S", led))

    return vermelho, azul, estrela, led

def principal():
    vermelho, azul, estrela, led = listas()

    print(vermelho)
    print(azul)
    print(estrela)
    print(led)

#Programa principal
principal()