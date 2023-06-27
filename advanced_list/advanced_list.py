import argparse

parser = argparse.ArgumentParser(description='Search for words including partial word')
parser.add_argument('snippet', help='partial (or complete) string to search for in words')
#Valida o argparses
args = parser.parse_args()
#Coleta a variavel snippet
snippet = args.snippet.lower()
#Abre o arquivo com as palavras
with open('/usr/share/dict/words') as f:
    words = f.readlines()
#Instancia uma lista vazia
matches = []
#Percorre todo o arquivo words procurando por palavras relacionas
for word in words:
    if snippet in word.lower():
        matches.append(word)
print(matches)