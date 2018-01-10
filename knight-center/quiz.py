ministro = input("quais nomes de ministros vc consegue lembrar?")

ministroSplit = ministro.split(",")

print(ministroSplit)

ministroLower = [nome.lower() for nome in ministroSplit]

print(ministroLower)

listaMinistro = ["Grace Mendonça", "Grace", "Mendonça", "Blairo Maggi", "Blairo", "Maggi", "Ilan Goldfajn", "Ilan", "Goldfajn", "Eliseu Padilha", "Eliseu", "Padilha", "Alexandre Baldy", "Alexandre", "Baldy", "Gilberto Kassab", "Gilberto", "Kassab", "Sérgio Sá Leitão", "Sérgio", "Sá", "Leitão", "Sá Leitão", "Luislinda Valois", "Luislinda", "Valois", "Wagner de Campos Rosário", "Wagner", "de Campos Rosário", "Rosário", "Mendonça Filho", "Mendoncinha", "Raul Jungmann", "Raul", "Jungmann", "Osmar Terra", "Osmar", "Terra", "Marcos Pereira", "Marcos", "Pereira", "Leonardo Picciani", "Leonardo", "Picciani", "Henrique Meirelles", "Henrique", "Meirelles", "Helder Barbalho", "Helder", "Barbalho", "Torquato Jardim", "Torquato", "Jardim", "Sarney Filho", "Fernando Bezerra Coelho Filho", "Fernando Coelho", "Fernando", "Coelho Filho", "Bezerra Coelho Filho", "Dyogo Oliveira", "Dyogo", "Oliveira", "Aloysio Nunes Ferreira", "Aloysio Nunes", "Aloysio", "Ricardo Barros", "Ricardo", "Barros", "Carlos Marun", "Marun", "Carlos",
"Wellington Moreira Franco", "Moreira Franco", "Sérgio Etchegoyen", "Etchegoyen", "Sérgio", "Cristiane Brasil", "Cristiane", "Maurício Quintella Lessa", "Maurício Quintella", "Quintella Lessa", "Maurício", "Marx Beltrão", "Beltrão", "Marx"]

listaMinistroLower = [lista.lower() for lista in listaMinistro]

print(listaMinistroLower)

if ministroLower in listaMinistroLower:
    print("vc acertou algum ministro")
else:
    print("tente de novo")