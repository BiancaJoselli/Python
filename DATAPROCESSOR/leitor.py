import csv
import json
import os

def _para_int(valor, padrao=None):
    try: 
        return int(valor)
    except (ValueError, TypeError):
        return padrao


def _para_float(valor, padrao=None):
    try:
        return float(valor)
    except (ValueError, TypeError):
        return padrao


def carregar_clientes(caminho):
    if not os.path.exists(caminho):
        print(f"[ERRO] Arquivo não encontrado: {caminho}")
        return []

    clientes = []
    with open(caminho, encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            clientes.append({
                "id": _para_int(linha["id"]),
                "nome": linha["nome"].strip(),
                "email": linha["email"].strip(),
                "idade": _para_int(linha["idade"]),
                "cidade": linha["cidade"].strip(),
                "data_cadastro": linha["data_cadastro"].strip(),
            })
            clientes.append(cliente)
    return clientes

def carregar_config(caminho):
    if not os.path.exists(caminho):
        print(f"[ERRO] Arquivo não encontrado: {caminho}")
        return {}

    with open(caminho, encoding="utf-8") as arquivo:
        return json.load(arquivo)
