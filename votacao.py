candidatoA = int(input("candidatoa"))
candidatoB = int(input("candidatob"))
candidatoC = int(input("candidatoc"))
brancos = int(input("brancos"))
nulos = int(input("nulos"))
eleitoresT = (float(candidatoA)+float(candidatoB)+float(candidatoC)+float(brancos)+float(nulos))
votosA = (float(candidatoA)*float(eleitoresT))/100
votosB = (float(candidatoB)*float(eleitoresT))/100
votosC = (float(candidatoC)*float(eleitoresT))/100
brancos = (float(brancos)*float(eleitoresT))/100
nulos = (float(nulos)*float(eleitoresT))/100
print("eleitoresT", eleitoresT)
print("votosA", votosA)
print("votosB", votosB)
print("votosC", votosC)
print("brancos", brancos)
print("nulos", nulos)

