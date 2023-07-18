#Importando o range para numero aleatorio

def executa():

    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana"
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

        chute = input("Qual letra? ")
        #Strip remove espacos
        chute = chute.strip().lower()

        index = 0
        if(chute in palavra_secreta):
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = chute
                index += 1
        else:
            tentativas -= 1
            print("Voce possui {} tentativas".format(tentativas))
        enforcou = tentativas == 0
        acertou = '_' not in letras_acertadas
            
            #Mesma coisa do de cimea
            #index = index + 1
        print(letras_acertadas)



#Pega o parametro passado no comando se possui o nome do arquivo
if(__name__== "__main__"):
    executa()
