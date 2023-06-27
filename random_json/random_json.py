import random
import os
import json

#Seta a variavel com a quantidade de arquivos que sera gerado
count = int(os.getenv("FILE_COUNT") or 10)
#Carrega as palavras la do arquivo words
words = [word.strip() for word in open('/usr/share/dict/words').readlines()]
#Cria uma variavel vazia onde vai repetir ate o count
for identifier in range(count):
    #Gera um numero
    amount = random.uniform(1.0, 1000)
    #Cria o conteudo json com os valores aleatorios
    content = {
        #Random choice e uma funcao que escolhe um item da lista
        'topic': random.choice(words),
        'value': "%.2f" % amount
    }
    #Imprime cada arquivo com o nome identifier com o content acima
    with open(f'./output/receipt-{identifier}.json', 'w') as f:
        #Ira fazer a escrita do content passando o arquivo aberto acima como parametro
        json.dump(content, f)