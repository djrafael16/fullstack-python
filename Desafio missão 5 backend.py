def verificar_senha():
    senha_correta = "Python123"
    try:
        senha_digitada = input("Digite a senha: ")
        
        if senha_digitada == senha_correta:
            print("Acesso concedido!")
        else:
            print("Senha incorreta. Tente novamente.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Chama a função
verificar_senha()