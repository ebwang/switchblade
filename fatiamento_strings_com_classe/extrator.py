class ExtratorURL:
    def __init__(self,url, parameter):
        self.set_url(url)
        self.parameter = parameter

    #Normaliza a url sem espaco e tudo caixa baixa
    def set_url(self,url):
        self.url = url.lower().strip()

    #Verifica a posicao do ?
    def get_position_question(self):
        return self.url.find('?')

    #Pega a primeira parte da url antes do interrogacao
    def get_url_base(self):
        return self.url[:self.get_position_question()]

    #Pega a parte da url apos o interrogacao
    def get_url_parameters(self):
        return self.url[self.get_position_question()+1:]

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
    
            
             
extrator = ExtratorURL("https://globo.com/teste?query=noticias&local=alagoas", "local")
print(extrator.get_url_base())
print(extrator.get_url_parameters())
print(extrator.get_initial_parameter_position())
print(extrator.get_position_ampersand())
print(extrator)