# -*- encoding: utf-8 -*-

import csv

pessoas = {}

csv_file = open("../Music/dadosPlenario/plenarioVotacoesFinalsocial.csv", "r")

linhas = csv.reader(csv_file, delimiter=",", quotechar='"')

for data in linhas:
	nome = data[2]
	partido = data[3]
	uf = data[4]
	#twitter = data[5]
	#facebook = data[6]
	#instagram = data[7]
	pessoas[nome] = partido + "-" + uf

	print(pessoas)