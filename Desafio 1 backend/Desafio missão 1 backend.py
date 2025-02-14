def verificar_aprovacao(nota):
    if nota >= 6:
        return "Aprovado"
    else:
        return "Reprovado"

# Entrada do usuário
try:
    nota = float(input("Digite a nota do aluno: "))
    if 0 <= nota <= 10:
        print("Resultado:", verificar_aprovacao(nota))
    else:
        print("Erro: A nota deve estar entre 0 e 10.")
except ValueError:
    print("Erro: Digite um valor numérico válido.")