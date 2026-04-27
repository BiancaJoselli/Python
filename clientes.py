clientes = [
    {
        "id": 1,
        "nome": "João Silva",
        "email": "joao.silva@email.com",
        "idade": 34,
        "cidade": "Joinville",
        "data_cadastro": "2023-01-10"
    },
    {
        "id": 2,
        "nome": "Maria Souza",
        "email": "maria@email",      # email inválido
        "idade": 28,
        "cidade": "Florianopolis",
        "data_cadastro": "2023-02-15"
    },
    {
        "id": 3,
        "nome": "Carlos Pereira",
        "email": "carlos.pereira@email.com",
        "idade": -5,                  # idade inválida
        "cidade": "Curitiba",
        "data_cadastro": "2023-03-20"
    },
    {
        "id": 4,
        "nome": "Ana Lima",
        "email": "ana.lima@email.com",
        "idade": 45,
        "cidade": "Joinville",
        "data_cadastro": "2023-01-25"
    },
    {
        "id": 5,
        "nome": "Pedro Santos",
        "email": "",                  # email vazio
        "idade": 38,
        "cidade": "Sao Paulo",
        "data_cadastro": "2023-02-30" # data inválida
    },
]

# Imprimir todos os clientes
for cliente in clientes:
    print(f"ID {cliente['id']}: {cliente['nome']} | {cliente['cidade']}")

print(f"Total de clientes: {len(clientes)}")

cidades = [cliente["cidade"] for cliente in clientes]
print(cidades)
# ['Joinville', 'Florianopolis', 'Curitiba', 'Joinville', 'Sao Paulo']

cidades_unicas = list(set(cidades))
print(cidades_unicas)