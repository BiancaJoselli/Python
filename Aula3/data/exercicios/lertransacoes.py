import csv

def carregar_transacoes(caminho):
    def para_int(v, pad=None):
        try:
            return int(v)
        except (ValueError, TypeError):
            return pad

    def para_float(v, pad=None):
        try:
            return float(v)
        except (ValueError, TypeError):
            return pad

    transacoes = []
    with open(caminho, encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            transacao = {
                "id": para_int(linha["id"]),
                "cliente_id": para_int(linha["cliente_id"]),
                "valor": para_float(linha["valor"]),
                "categoria": linha["categoria"].strip(),
                "data": linha["data"].strip(),
                "status": linha["status"].strip(),
            }
            transacoes.append(transacao)
    return transacoes

print(carregar_transacoes("transacoes.csv"))