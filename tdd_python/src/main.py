

# Press the green button in the gutter to run the script.
from src.dominio import Avaliador, Leilao, Usuario, Lance

if __name__ == '__main__':
    gui = Usuario('Gui')
    yuri = Usuario('Yuri')

    lance_do_yuri = Lance(yuri, 100.0)
    lance_do_gui = Lance(gui, 150.0)

    leilao = Leilao('Celular')

    leilao.lances.append(lance_do_yuri)
    leilao.lances.append(lance_do_gui)


    avaliador = Avaliador()
    avaliador.avalia(leilao)

    print(f'Maior lance: {avaliador.maior_lance}')
    print(f'Menor lance: {avaliador.menor_lance}')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
