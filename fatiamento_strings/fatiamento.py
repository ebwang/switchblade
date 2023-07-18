#Quebrando a url entre a base e os parametros passados
#Slicing url
url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar".lower()
indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]
url_parametros = url[indice_interrogacao+1:]


#A seguir criamos um indice a partir da palavra buscada pegando o seu comprimento
#parametro_busca = 'quantidade'
#Podemos buscar outros parametros
parametro_busca = 'moedaOrigem'.lower()
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1

#Por ultimo queremos tratar o & pois podem haver varios parametros
#Como estamos buscando da url parametros temos que impor que ele começe a partir do indice do parametro buscado, senao ele vai retornar um valor inferior
indice_e_comercial = url_parametros.find('&', indice_valor)
if indice_e_comercial == -1:
    #Nesse caso ele sabe que e a ultima palavra, pois estamos buscando do indice do parametro ate o final
    valor = url_parametros[indice_valor:]
else:
    #Ele assume uma palavra do meio que esta no meio da url_parametros
    valor = url_parametros[indice_valor:indice_e_comercial]
print(valor)