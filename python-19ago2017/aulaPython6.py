#nome e idade, depois só os nomes de quem tem mais de 25
 
dicionario ={}
 
while(True):
    nome = input('Informe o nome do aluno ou s para sair: ')
    if nome == 's':
        break
    idade = input('Informe a idade do aluno {}'.format(nome))
    dicionario[nome]= int(idade)
 
maiores = (nome for nome, idade in dicionario.items() if idade > 25)
print("\n".join(maiores))