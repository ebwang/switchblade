class Funcionario:
    #Essa classe esta sendo incializada com esse nome porem quem retorna o metodo dessa variavel e a classe Hipster
    #Ou seja herdamos o comportamento
    def __init__(self, nome):
        self.nome = nome

    def registra_horas(self, horas):
        print('Horas registradas.')

    def mostrar_tarefas(self):
        print('Fez muita coisa...')

class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer')

    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')

class Alura(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Alurete!')

    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum')


#Estamos somente usando esse instanciamento dessa classe q retorna o duck typing tipo string
class Hipster:
    def __str__(self):
        return f'Hipster,  {self.nome}'

class Junior(Alura):
    pass

#Essa classe vai usar a classe Hipster
class Pleno(Alura, Caelum, Hipster):
    pass


jose = Junior('Jose')
jose.busca_perguntas_sem_resposta()

luan = Pleno('Luan')
luan.busca_perguntas_sem_resposta()
luan.busca_cursos_do_mes()
luan.mostrar_tarefas()

print(luan)