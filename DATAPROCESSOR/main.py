from leitor import carregar_clientes, carregar_transacoes, carregar_config

clientes = carregar_clientes("data/clientes.csv")
transacoes = carregar_transacoes("data/transacoes.csv")
config = carregar_config("data/config.json")

print(f"Clientes carregados: {len(clientes)}")
print(f"Transações carregadas: {len(transacoes)}")
print(f"Configuração: {config}") 