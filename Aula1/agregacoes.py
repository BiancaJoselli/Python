clientes = [
    {"id": 1, "nome": "João Silva", "email": "joao.silva@email.com",
        "idade": 34, "cidade": "Joinville"},
    {"id": 2, "nome": "Maria Souza", "email": "maria@email",
        "idade": 28, "cidade": "Florianopolis"},
    {"id": 3, "nome": "Carlos Pereira", "email": "carlos.pereira@email.com",
        "idade": -5, "cidade": "Curitiba"},
    {"id": 4, "nome": "Ana Lima", "email": "ana.lima@email.com",
        "idade": 45, "cidade": "Joinville"},
    {"id": 5, "nome": "Pedro Santos", "email": "",
        "idade": 38, "cidade": "Sao Paulo"},
]
def media_idade(clientes):
    idades_validas = [c["idade"] for c in clientes if c["idade"] > 0]

    if not idades_validas:
        return None  # Sem dados válidos para calcular

    return sum(idades_validas) / len(idades_validas)

media = media_idade(clientes)
print(f"Média de idade (dados válidos): {media:.2f}")
# Média de idade (dados válidos): 36.3