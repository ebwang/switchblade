#Importando o range para numero aleatorio
import random

def executa():

    imprime_mensagem_abertura()

    palavra_secreta = carrega_palavra_secreta()


    enforcou = False
    acertou = False

    #letras_acertadas = ["_", "_", "_", "_", "_", "_"]
    # Esse cara vai inicializar dinacamente com o recurso List Comprehension 
    # Porem poderia ser um append do "_" traves do len
    letras_acertadas = ["_" for letra in palavra_secreta]

    tentativas = 6
    print("Voce possui {} tentativas".format(tentativas))
    
    print(letras_acertadas)
    while(not enforcou and not acertou):
        chute = carrega_chute()

        if(chute in palavra_secreta):
            marca_chute_correto(chute,letras_acertadas,palavra_secreta)
        else:
            tentativas -= 1
            print("Voce possui {} tentativas".format(tentativas))
        enforcou = tentativas == 0
        acertou = '_' not in letras_acertadas
            
            #Mesma coisa do de cimea
            #index = index + 1
        print(letras_acertadas)

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1

def carrega_chute():
    chute = input("Qual letra? ")
    #Strip remove espacos
    chute = chute.strip().lower()
    return chute
    

def carrega_palavra_secreta():
    palavras = []
    
    with open("palavras.txt") as arquivo:
        for linha in arquivo:
            palavras.append(linha.strip())
    
    palavra_secreta = palavras[random.randrange(0,len(palavras))]
    return palavra_secreta

def imprime_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

#Pega o parametro passado no comando se possui o nome do arquivo
if(__name__== "__main__"):
    executa()
