# Complete o programa!

# a)
def loadFile(fname, lst):
	lst = []
	file = open(fname, 'r')
	i = 0
	file.readline()
	for line in file:
		line.split('\t')
		line.append(lst)
		i += 1
	file.close()
	return lst
    
# b) Crie a função notaFinal aqui...
def notaFinal(reg):
	nota = (reg[-1]+reg[-2]+reg[-3]/3)
	return nota

# c) Crie a função printPauta aqui...
def printPauta(lst):
	print('{:<6}{:^65}{:>4}'.format('Numero','Nome','Nota'))
	for e in lst:
		print("{:>6} {:^65} {:>4.1f}".format(e[0],e[1],notaFinal(e)))

# d)
def main():
    lst = []
    # ler os ficheiros
    loadFile("school1.csv", lst)
    loadFile("school2.csv", lst)
    loadFile("school3.csv", lst)
    
    # ordenar a lista
    ...
    
    # mostrar a pauta
    ...


# Call main function
if __name__ == "__main__":
    main()
