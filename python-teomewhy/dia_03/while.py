#%%
numero = 2
count = 1

while count <= 100:
    print(numero, "X", count, "=", numero * count)
    count += 1

# %%

count = 4
while count <= 100:
    resto = count % 4
    if resto == 0:
        print(count)

    count += 1
# %%

num = 2
while num <= 100:
    eh_primo = True
    divisor = 2

    while divisor < num:
        if num % divisor == 0:
            eh_primo = False
            break
        divisor += 1

    if eh_primo:
        print(num)

    num += 1
# %%

