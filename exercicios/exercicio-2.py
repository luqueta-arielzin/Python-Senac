print("SISTEMA DE LOGIN")

email = "admin@email.com"
senha = "123456"

email_input = input("e-mail: ")
senha_input = (input(" senha: "))

if email_input == email and senha_input == senha:
    print("Login realizado com sucesso!")
    print(f"Email: {email}")
    print(f"Senha: {senha}")
else: 
    print("Dados incorretos")
