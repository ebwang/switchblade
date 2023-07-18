#Importando o range para numero aleatorio
import random

def jogar():

    print("************************************")
    print("***Bem vindo ao jogo da Adivinhar!**")
    print("************************************")

    numero = random.randrange(1,100)
    tentativas = 0
    rodada = 1
    pontos = 1000

    print(numero)
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        tentativas = 20
    elif (nivel == 2):
        tentativas = 10
    else:
        tentativas = 5

    #Subistutuido pelo for
    #while(rodada <= tentativas):

    #Esse +1 pq senao termina com 2 tentativas pq a posicao final nao e inclusiva
    for rodada in range(1,tentativas+1):
        #Poderia ser da seguinte forma tbm a interpolacao de string
        print(f"Tentativa {rodada} de {tentativas}")
        #print("Tentativa {} de {}".format(rodada, tentativas))
        chute = int(input("Digite seu numero: "))
        print("Voce digitou", chute)

        # Vai pular o resto da execucao do for
        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero
        maior = chute > numero
        menor = chute < numero

        #A pontuacao e o numero secreto menos o chute
        #Caso o chute for maior que o numero secreto entao o abs tira o sinal negativo ex: 30-60 = 30 pts com abs
        pontos_perdidos = abs(numero - chute)
        pontos = pontos - pontos_perdidos

        if acertou:
            print("Voce acertou")
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        elif maior:
            print("Seu chute foi maior que o numero")
            if (rodada == tentativas):
                print("O número secreto era {}. Você fez {}".format(numero, pontos))
        elif menor:
            print("Seu chute foi menor")
            if (rodada == tentativas):
                print("O número secreto era {}. Você fez {}".format(numero, pontos))
        #Nao precisa substituido pelo for
        #rodada = rodada + 1
    print("Fim de jogo")


#Pega o parametro passado no comando se possui o nome do arquivo
if( __name__ == "__main__"):
    jogar()