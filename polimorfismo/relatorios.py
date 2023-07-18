class Relatorio:
    def gera_relatorio(self):
        print('Relatório geral')
    #Faz a mesam coisa de cima    
    def __str__(self):
        return 'Relatório geral'

class RelatorioUsuarios(Relatorio):
    def gera_relatorio(self):
        print('Relatório dos usuários')
    #Faz a mesma coisa de cima    
    def __str__(self):
        return 'Relatório de usuarios'

class RelatorioCustos(Relatorio):
    def gera_relatorio(self):
        print('Relatório de custos')
    #Faz a mesma coisa de cima
    def __str__(self):
        return 'Relatório de custos'

relatorio1 = RelatorioUsuarios()
relatorio2 = RelatorioCustos()
relatorio3 = RelatorioUsuarios()
relatorio4 = RelatorioUsuarios()

relatorios = [relatorio1, relatorio2, relatorio3, relatorio4]
for rel in relatorios:
    rel.gera_relatorio()
    #Ele usa o metodo __str__
    print(rel)