import re

class Conversor:
    def convert(self, moedaorigem, moedadestino, quantidade):
        if(moedaorigem == "dolar" and moedadestino == "real"):
            valor_final = quantidade * 5.50
            return "Seu valor final foi de R${}".format(valor_final)
        elif(moedaorigem == "real" and moedadestino == "dolar"): 
            valor_final = quantidade / 5.50
            return "Seu valor final foi de US${}".format(valor_final)
        

class ExtratorURL:
    def __init__(self,url):
        self.set_url(url)
        self.parameter = ''

    #Normaliza a url sem espaco e tudo caixa baixa
    def set_url(self,url):
        if not url:
            raise ValueError("A URL esta vazia")
        else:
            self.url = url.lower().strip()

        #Chamamos o metodo compile para validar a  url com o padrao que queremos
        #Parenteses e usado para informar que e a string exata que queremos
        #O interrogacao informa que pode vir ou nao, por exemplo https ou http
        padrao_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
        #Qdo comparamos uma string inteira com o padrao que queremos usamos match, caso queremos encontrar um padrao de string dentro da strng usamos search
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError("A URL não é válida.")

    #Verifica a posicao do ?
    def get_position_question(self):
        return self.url.find('?')

    #Pega a primeira parte da url antes do interrogacao
    def get_url_base(self):
        return self.url[:self.get_position_question()]

    #Pega a parte da url apos o interrogacao
    def get_url_parameters(self):
        return self.url[self.get_position_question()+1:]

    
    def get_parameter_value(self, parameter):
        self.parameter = parameter.lower().strip()
        return f'{self.check_final_apersand()}'
        
    
    #Pega a posicao inicial da palavra que queremos da url parameters
    # ou seja estamos pegando essa posicao: local=alagoas
    #                                       ^

    def get_initial_parameter_position(self):
        return self.get_url_parameters().find(self.parameter)

    #Pega a posicao inicial do valor, somamos o valor do parametro + 1 pq e explicito
    # ou seja estamos pegando essa posicao: local=alagoas
    # OBS sem o +1 iria pegar o 'l'              ^
    def get_initial_value_position(self):
         return self.get_initial_parameter_position() + len(self.parameter) + 1
    
    #Verifica a posicao do & comercial
    def get_position_ampersand(self):
        return self.get_url_parameters().find('&', self.get_initial_value_position())

    #Verifica se realmente o & existe
    #Caso retorne -1 e pq o & comercial nao existe, ou seja a ultima palavra
    def check_final_apersand(self):
        if (self.get_position_ampersand() == -1):
            return self.get_url_parameters()[self.get_initial_value_position():]
        else:
            return self.get_url_parameters()[self.get_initial_value_position():self.get_position_ampersand()]

    #Metodo de saida padrao        
    def __str__(self):
        return f'{self.check_final_apersand()}'
    
            
             
extrator = ExtratorURL("bytebank.com/cambio?quantidade=100&moedaOrigem=dolar&moedaDestino=real")
print(extrator.get_parameter_value('moedadestino'))
conversor = Conversor()
print(conversor.convert("real","dolar",100))