#Faça um programa que vende uma garrafa de água:
#Se o cliente escolher água mineral natural, será cobrado R$1,50
#Se o cliente escolher água mineral com gás, será cobrado R$2,50

print("Escolha a garrafa de água: \n 1 - Água mineral natural \n 2 - Água mineral com gás")
garrafa=input("Insira o numero da garrafa que quer: ")

if garrafa == "1":
    print("Valor a ser cobrado R$1,50")

elif garrafa == "2":
    print("Valor a ser cobrado R$2,50")

else: 
    print("Produto não reconhecido!")



#Resolucão Professor 

texto = """Escolha a sua água para comprar
(1) Água mineral natural 
(2) Água mineral com gás
"""

opcao = input(texto)

if opcao == "1":
    print("Sua conta deu: R$1,50")

elif opcao == "2":
    print("Sua conta deu: R$2,50")

else:
    print("Insira a opcão correta!")