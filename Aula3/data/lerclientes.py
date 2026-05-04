
import csv

def carregar_clientes(caminho):
    clientes = []
    with open(caminho, encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            clientes.append(dict(linha))
    return clientes

clientes = carregar_clientes("data/clientes.csv")
print(f"{len(clientes)} clientes carregados.")