def contar_letras(nome):
    nome_limpo = nome.strip()  # Remove espaços extras no início e no fim
    return f"O nome '{nome_limpo}' tem {len(nome_limpo.replace(' ', ''))} letras."

# Solicita um nome ao usuário
nome = input("Digite um nome: ")
print(contar_letras(nome))