preço = float(input("QUAL O PREÇO DO PRODUTO? R$"))
desconto = float(input("QUAL É O DESCONTO?"))
novo = preço - (preço * desconto / 100)
print("novo", novo)