import pytest

from src.dominio import Usuario, Leilao, Lance


def test_subtrai_valor_da_carteira():
    vini = Usuario('Vini', 500)
    leilao = Leilao('Celular')
    lance_vini = Lance(vini, 200)
    leilao.propoe(lance_vini)

    assert vini.carteira == 500.0
