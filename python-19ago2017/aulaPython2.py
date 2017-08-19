# -*- encoding: utf-8 -*-

idades = []

for i in range(10):
	idade = input("informe idade ou s para sair \n")
	idade = int(idade)
	idades.append(idade)

#print(idades)

soma = 0

for i in idades:
	soma += i
qtd_elementos = len(idades)

media = float(soma) / qtd_elementos

print ("minha média de idade é %0.4f \n" % media)

