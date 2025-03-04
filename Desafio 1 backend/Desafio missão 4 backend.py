def soma_dois_numeros():
    try:
        # Solicita dois números ao usuário
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        
        # Calcula a soma
        soma = num1 + num2
        
        # Exibe o resultado
        print(f"A soma de {num1} e {num2} é {soma}")
    except ValueError:
        print("Erro: Por favor, insira apenas números válidos.")

# Chama a função
soma_dois_numeros()