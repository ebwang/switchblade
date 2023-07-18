
"""# Dicionário (Mapa etc)"""

aparicoes = {
  "Guilherme" : 1,
  "cachorro" : 2,
  "nome" : 2,
  "vindo" : 1
}

type(aparicoes)

aparicoes["Guilherme"]

aparicoes["cachorro"]

#Quando vc chama o dicionario sem a key existir ele vai estourar um erro
aparicoes["xpto"]

#Melhor maneira de verificar se o conteudo existe e com o get no dicionario
#Ele nao vai quebrar o programa 
aparicoes.get("xpto", 0)

aparicoes.get("cachorro", 0)

aparicoes = dict(Guilherme = 2, cachorro = 1)
aparicoes

#Se o conteudo ja existir ele sobsreve a chave com seu valor novo
aparicoes = {
  "Guilherme" : 1,
  "cachorro" : 2,
  "nome" : 2,
  "vindo" : 1
}

#Adiciona um item ao dicionario com sua chave valor
aparicoes["Carlos"] = 1

aparicoes

#Atualiza o valor de Carlos
aparicoes["Carlos"] = 2

aparicoes

#Apaga o item do dicinario
del aparicoes["Carlos"]

aparicoes

#Verifica se o item existe no dicionario
"cachorro" in aparicoes

"Carlos" in aparicoes

#So vai imprimir a key sem seu valor
for elemento in aparicoes:
  print(elemento)

#Mesmo de cima
for elemento in aparicoes.keys():
  print(elemento)

#Imprime somente o valor
for elemento in aparicoes.values():
  print(elemento)

1 in aparicoes.values()

#Imprime a key e seu valor
for elemento in aparicoes.keys():
  valor = aparicoes[elemento]
  print(elemento, valor)

#O Items pega a key e valor
for elemento in aparicoes.items():
  print(elemento)

#Ele consegue iterar diretamente com key e valor
for chave, valor in aparicoes.items():
  print(chave, "=", valor)

#Imprime a palavra em cada interacao de dicionario
["palavra {}".format(chave) for chave in aparicoes.keys()]
