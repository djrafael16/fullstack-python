def pode_votar(idade):
    if idade >= 16:
        return "Pode votar"
    else:
        return "Não pode votar"

# Entrada do usuário
try:
    idade = int(input("Digite sua idade: "))
    if idade >= 0:
        print("Resultado:", pode_votar(idade))
    else:
        print("Erro: A idade não pode ser negativa.")
except ValueError:
    print("Erro: Digite um valor numérico válido.")13
    