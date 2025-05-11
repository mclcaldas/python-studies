#Faça um programa que verifique se a pessoa pertence à família “calvo”.

nome = input("Digite seu nome completo: ")

if "calvo" in nome:
    print("você pertence à família Calvo!")
else:
    print("você não pertence à família Calvo.")


#Faça um programa que verifique se a pessoa pertence à família “calvo” ou “silva”.

nome_completo = input("Digite seu nome completo: ")

if "calvo" or "silva" in nome:
    print("você pertence à família Calvo ou Silva")
else:
    print("você não pertence à família Calvo ou Silva")

