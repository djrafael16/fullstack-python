def classificar_nota(nota):
    if 90 <= nota <= 100:
        return "Parabéns, você tirou A!"
    elif 80 <= nota <= 89:
        return "Muito bem, você tirou B."
    elif 70 <= nota <= 79:
        return "Bom trabalho, você tirou C."
    elif 60 <= nota <= 69:
        return "Fique atento, você tirou D."
    else:
        return "Estude um pouco mais, você tirou F."

# Entrada do usuário
try:
    nota = float(input("Digite a nota do aluno: "))
    if 0 <= nota <= 100:
        print("Resultado:", classificar_nota(nota))
    else:
        print("Erro: A nota deve estar entre 0 e 100.")
except ValueError:
    print("Erro: Digite um valor numérico válido.")
