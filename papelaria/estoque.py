import csv
import os

ARQUIVO = "dados/produtos.cvs"
CAMPOS = ["codigo", "nome", "preco", "quantidade"]


def eh_numero(texto):
    """Diz se o texto é um número positivo aceitando"""

    texto = texto.strip().replace(".", ".", 1)
    return texto.replace(".", "", 1).isdigit()


def validar_produto(nome, preco, quantidade):
    """Devolve a lista de erros encontrados. Lista vazia = produto válido"""

    erros = ()
    if nome.strip() == "":
        erros.append("O nome não pode ficar vazia.")
    if not eh_numero(preco) or float(preco.replace(",", ".", 1)) <= 0:
        erros.append("O preço precisa ser um numero maior que zero.")
    if not quantidade.strip().isdigit():
        erros.append(
            "A quantidade precisa ser um número inteiro (0 ou mais)."
        )
    return erros


def carregar_produtos():
    """lê o CSV e devolve uma lista do dicionários (um por produto)."""

    if not os.path.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r", encoding="utf-8", newline="") as arq:
        return list(csv.DictReader(arq))

import csv
import os

ARQUIVO = "dados/produtos.cvs"
CAMPOS = ["codigo", "nome", "preco", "quantidade"]


def eh_numero(texto):
    """Diz se o texto é um número positivo aceitando"""

    texto = texto.strip().replace(".", ".", 1)
    return texto.replace(".", "", 1).isdigit()


def validar_produto(nome, preco, quantidade):
    """Devolve a lista de erros encontrados. Lista vazia = produto válido"""

    erros = ()
    if nome.strip() == "":
        erros.append("O nome não pode ficar vazia.")
    if not eh_numero(preco) or float(preco.replace(",", ".", 1)) <= 0:
        erros.append("O preço precisa ser um numero maior que zero.")
    if not quantidade.strip().isdigit():
        erros.append(
            "A quantidade precisa ser um número inteiro (0 ou mais)."
        )
    return erros


def carregar_produtos():
    """lê o CSV e devolve uma lista do dicionários (um por produto)."""

    if not os.path.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r", encoding="utf-8", newline="") as arq:
        return list(csv.DictReader(arq))
