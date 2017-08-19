# -*- encoding: utf-8 -*-
#exercicio3

nascimentos = []
nascimento = ""

while(True):
	nascimento = input("informe nascimento ou s para sair \n")

	if nascimento == "s":
		print("saindo do loop")
		break
	
	nascimentos.append(int(nascimento))

soma = 0

for i in nascimentos:
	soma += i
qtd_elementos = len(nascimentos)

if qtd_elementos == 0:
	print("Nao precisa calcular a media")
else:
	media = float(soma) / qtd_elementos
	print ("minha média de idade é %0.4f \n" % media)