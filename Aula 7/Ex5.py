#a)
def teams():
	equipas_feitas = []
	print('Para terminar de acrescentar equipas prima enter')
	while True:
		equipa = input('Equipa a adicionar:')
		if equipa == '':
			return equipas_feitas
		else:
			equipas_feitas.append(equipa)
#b)
def matchmaking(equipas):
	match = []
	for c1 in range(len(equipas)):
		for c2 in range(len(equipas)):
			if c1!= c2:
				match.append((equipas[c1], equipas[c2]))
	return match
	
def results(jogos):
	results_c = {}
	for game in jogos:
		print(game)
		resultado = input('Resultado:')
		resultado = tuple(resultado.split(','))
		results_c[game] = resultado
	return results_c
	
def equipas_atualizadas(resultados):
	dic = {}
	for equipa1, equipa2 in resultados:
		golos1 = int(resultados[equipa1,equipa2][0])
		golos2 = int(resultados[equipa1,equipa2][1])
		if equipa1 not in dic:
			dic[equipa1]=[0,0,0,0,0]
		if equipa2 not in dic:
			dic[equipa2]=[0,0,0,0,0]
		vit_1,der_1,golo_marc_1,golo_sof_1,pontos1 = dic[equipa1]
		vit_2,der_2,golo_marc_2,golo_sof_2,pontos2 = dic[equipa2]	
		if golos1 > golos2:
			vit_1 += 1
			golo_marc_1 += golos1
			golo_sof_1 += golos2
			pontos1 += 3
			
			der_2 += 1
			golo_marc_2 += golos2
			golo_sof_2 += golos1
		elif golos2 > golos1:
			vit_2 += 1
			golo_marc_2 += golos2
			golo_sof_2 += golos1
			pontos2 += 3
			
			der_1 += 1
			golo_marc_1 += golos1
			golo_sof_1 += golos2
		else:
			golo_marc_1 += golos1
			golo_sof_1 += golos2
			pontos1 += 1
			
			golo_marc_2 += golos2
			golo_sof_2 += golos1
			pontos2 += 1
			
		dic[equipa1] = [vit_1,der_1,golo_marc_1,golo_sof_1,pontos1]
		dic[equipa2] = [vit_2,der_2,golo_marc_2,golo_sof_2,pontos2]
	return dic	
			
def imprimir(estatistica):
	print('{:<25s}{:15s}{:15s}{:15s}{:15s}{:15s}'.format('Equipa','Vitorias','Derrotas','Golos Marcados','Golos Sofridos','Pontos'))
	for a in sorted(estatistica.items(),key=lambda x: x[1][4], reverse=True):
		print("{:<25s}{:^8}{:^20d}{:^20d}{:^15d}{:^10d}".format(a[0],a[1][0],a[1][1],a[1][2],a[1][3],a[1][4]))
"""
Faz se o print aqueles coisos todos e ordena se segundo o valor dos pontos 
e como se quer por ordem decrescente coloca-se a condiçao reverse
"""

#f
def winner(estatistica):
	maiores = {}
	maxim = 0 # ir buscar um valor ao dicionario dava demasiado trabalho e como os pontos das equipas sao de 0 para cima nao e por ai
	for a in estatistica:
		pontos = estatistica[a][4]
		if pontos > maxim:
			maxim = pontos
			equipa = a
	for valor in estatistica:
		if maxim == estatistica[valor][4]:
			maiores[valor] = estatistica[valor]
	
	if len(maiores) >= 2: # temos que ver entao a diferença entre golos marcados
		diferenca = -1000 # este valor tambem escolhi assim a sorte que tem o defeito de obrigar a diferenca a ser maior que este valor
		for b in maiores:
			dif = estatistica[b][2] - estatistica[b][3]
			if dif > diferenca:
				diferenca = dif
				equipa = b
	winner = equipa
	return equipa
"""
vamos ver os pontos de cada equipa e se esse valor for maior que o maximo
entao passa a ser esse o maximo
depois vamos ver a situaçao de se os pontos forem iguais, isto ficou
feito de uma forma pouco recomendavel porque vamos ler outra vez tudo
mas assim apanhamos todas as equipas com aqueles pontos
Depois vamos calcular a diferenca e a que tiver maior e a vencedora

e finalmente acabamos esta porcaria
"""
def main():
	equipas = teams()
	lista_jogos = matchmaking(equipas)
	resultados = results(lista_jogos)
	#serve de teste
	#resultados = {("slb","scp"): [2,1],("scp","slb"):[1,2]}
	estatistica = equipas_atualizadas(resultados)
	print(estatistica)
	print(imprimir(estatistica))
	print(winner(estatistica))

				
			
			
main()	
			
			
			
			
			
			
			
			
			
			
			
		
