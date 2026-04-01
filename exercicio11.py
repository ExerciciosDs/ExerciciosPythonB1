tentativa = 3
senha = input("Bem vindo ao terminal! Digite sua senha: ")
fechar = False
    
while fechar != True:
    if senha == "admin123":
        print("Acesso permitido.")
        fechar = True
        
    else:
        tentativa -= 1
        
        if tentativa == 0:
            print("Conta bloqueada.")
            fechar = True
            
        else:
            print("Senha incorreta! Você tem mais ",tentativa," tentativas.")
            senha = input("Digite sua senha: ")