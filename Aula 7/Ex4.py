def listContacts(dic):
	"""Print the contents of the dictionary as a table, one item per row."""
	print("{:>12s} : {:^22} : {:<12s}".format("Numero", "Nome", 'Morada'))
	for num in dic:
		print("{:>12s} : {:^22} : {:<12s}".format(num, dic[num][0], dic[num][1]))

def filterPartName(contactos):
	"""Returns a new dict with the contacts whose names contain partName."""
	nome = input('Nome/Parte do nome:')
	dic = {}
	for info in contactos:
		if nome in contactos[info[1]]:
			dic[info] = contactos[info]
	return dic

def addcontact(contactos):
	numero = input('Numero:')
	nome = input('Nome:')
	morada = input('Morada:')
	contactos[numero] = nome,morada
	return contactos

def removecontacts(contactos):
	numero = input('Numero a remover:')
	del contactos[numero]
	return contactos
	
def searchnumber(contactos):
	numero = input('Numero:')
	if numero in contactos:
		return contactos[numero]
	else:
		return numero
	
	
def menu():
	"""Shows the menu and gets user option."""
	print()
	print("(L)istar contactos")
	print("(A)dicionar contacto")
	print("(R)emover contacto")
	print("Procurar (N)úmero")
	print("Procurar (P)arte do nome")
	print("(T)erminar")
	op = input("opção? ").upper()   # converts to uppercase...
	return op


def main():
	"""This is the main function containing the main loop."""

	# The list of contacts (it's actually a dictionary!):
	contactos = {"234370200": ["Universidade de Aveiro",'Santiago, Aveiro'],
	
		"727392822": ["Cristiano Aveiro",'Rua Senhora das Dores'],
		"387719992": ["Maria Matos",'Rua zé manel'],
		"887555987": ["Marta Maia",'Coimbra'],
		"876111333": ["Carlos Martins",'Porto'],
		"433162999": ["Ana Bacalhau", 'Turol']
	}

	op = ""
	while op != "T":
		op = menu()
		if op == "T":
			print("Fim")
		elif op == "L":
			print("Contactos:")
			listContacts(contactos)
		elif op == 'A':
			addcontact(contactos)
		elif op == 'R':
			removecontacts(contactos)   
		elif op == 'N':
			print(searchnumber(contactos)) 
		elif op == 'P':
			print(filterPartName(contactos))
		else:
			print('Não implementado!')

# O programa começa aqui
main()
