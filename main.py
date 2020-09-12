
from Clases import *
from py2neo import *

def bubbleSort(alist):
	for passnum in range(len(alist)-1, 0, -1):
	for i in range(passnum):
			if alist[i].contador > alist[i+1].contador:
			temp = alist[i]
				alist[i] = alist[i+1]
				alist[i+1] = temp

def estaEnLista(lista, nombre):
	for i in range(len(lista)):
	if lista[i].nombre == nombre:
		return i
	return -1

string = """
 /$$$$$$$$ /$$$$$$$  /$$$$$$ /$$    /$$   /$$$$$$   /$$$$$$   /$$$$$$
|__  $$__/| $$__  $$|_  $$_/| $$   | $$  /$$__  $$ /$$__  $$ /$$__  $$
   | $$   | $$  \ $$  | $$  | $$   | $$ | $$  \ $$| $$  \__/| $$  \ $$
   | $$   | $$$$$$$/  | $$  |  $$ / $$/ | $$$$$$$$| $$ /$$$$| $$  | $$
   | $$   | $$__  $$  | $$   \  $$ $$/  | $$__  $$| $$|_  $$| $$  | $$
   | $$   | $$  \ $$  | $$    \  $$$/   | $$  | $$| $$  \ $$| $$  | $$
   | $$   | $$  | $$ /$$$$$$   \  $/    | $$  | $$|  $$$$$$/|  $$$$$$/
   |__/   |__/  |__/|______/    \_/	|__/  |__/ \______/  \______/
"""
sigue0 = True
while sigue0:
	print(string)
	nombre = input(
	    "Hola! ¿Cual es tu nombre? (Ingresa X para salir del programa)\n")
	d = graph.run("MATCH (n:Persona) WHERE n.nombre = '" +
	              nombre+"' RETURN n").data()
	if len(d) > 0:
	p = Persona()
		p.nombre = nombre
		graph.pull(p)
		sigue = True
		while sigue:
		des1 = input("Hola, "+nombre+"\n\t1. Tus gustos \n\t2. Tus Amigos\n\t3. Lugares visitados\n\t4. Sugerencia de Viaje\n\t5. Agregar lugar visitado\n\t6. Eliminar Amigo\n\t7.Salir\n")
			if (des1 == "1"):
			for gusto in p.likes:
				print(gusto.cualidad)
			elif(des1 == "2"):
			for amigo in p.amigos:
				print(amigo.nombre)
			elif(des1 == "3"):
				cOp = input("Deseas ver... \n\t1. Ciudades\n\t2. Paises\n")
				if cOp == "1":
					if (len(p.yaVisito) != 0):
					for l12 in p.yaVisito:
						print(l12.nombre)
					else:
					print("No has visitado ningun lugar :(")
				elif cOp == "2":
					if (len(p.yaVisitoP) != 0):
					for l12 in p.yaVisitoP:
						print(l12.nombre)
					else:
					print("No has visitado ningun lugar :(")
				else:
				print("Ese no es un dato valido....")
			elif(des1 == "4"):
				des = input(
				    "¿Que deseas que te recomiente?\n\t1. Un pais\n\t2. Una ciudad\n")
					listaLugares = []
					if (des == "1"):
					for like in p.likes:
						for pais in like.esP:
								numero = estaEnLista(listaLugares, pais.nombre)
								if (numero != -1):
								listaLugares[numero].sumar(5)
								else:
								temp = Lugar(pais.nombre)
									temp.sumar(5)
									listaLugares.append(temp)
						for amigo in p.amigos:
						for paisito in amigo.yaVisitoP:
								numero = estaEnLista(listaLugares, paisito.nombre)
								if numero != -1:
								listaLugares[numero].sumar(3)
								else:
								temp = Lugar(paisito.nombre)
									temp.sumar(3)
									listaLugares.append(temp)
							for pref in amigo.likes:
							for lugar in pref.esP:
									numero = estaEnLista(listaLugares, lugar.nombre)
									if numero != -1:
									listaLugares[numero].sumar(1)
									else:
									tmp = Lugar (lugar.nombre)
										tmp.sumar(1)
										listaLugares.append(tmp)
						bubbleSort(listaLugares)
						listaLugares.reverse()
						for i in listaLugares:
						print("\t"+i.nombre+" puntuacion: "+str(i.contador))

					elif (des =="2"):
					for like in p.likes:
						for lugar in like.es:
								numero = estaEnLista(listaLugares, lugar.nombre)
								if (numero != -1):
								listaLugares[numero].sumar(5)
								else:
								temp = Lugar(lugar.nombre)
									temp.sumar(5)
									listaLugares.append(temp)
						for amigo in p.amigos:
						for lugar in amigo.yaVisito:
								numero = estaEnLista(listaLugares, lugar.nombre)
								if numero != -1:
								listaLugares[numero].sumar(3)
								else:
								temp = Lugar(lugar.nombre)
									temp.sumar(3)
									listaLugares.append(temp)
							for pref in amigo.likes:
							for lugar in pref.es:
									numero = estaEnLista(listaLugares, lugar.nombre)
									if numero != -1:
									listaLugares[numero].sumar(1)
									else:
									tmp = Lugar (lugar.nombre)
										tmp.sumar(1)
										listaLugares.append(tmp)

						bubbleSort(listaLugares)
						listaLugares.reverse()
						for i in listaLugares:
						print("\t"+str(i.nombre)+" puntuacion: "+str(i.contador))
						print(str(len(listaLugares)))
					else:
					print("Ese valor no es valido :(")
			elif(des1 =="5"):
			cOp = input("¿Que has visitado?\n\t1. Ciudad\n\t2. Pais\n")
				if (cOp =="1"):
				lugarN = input("¿En donde has estado recientemente?\n")
					l = graph.run("MATCH (n:Ciudad) WHERE n.nombre = '"+ \
					              lugarN+"' RETURN n").data()
					if (len(l) >0):
					c = Ciudad()
						c.nombre = lugarN
						graph.pull(c)
						p.yaVisito.add(c)
						graph.push(p)
					else:
					print("Ese lugar no esta en la BD :(")
				elif(cOp =="2"):
				lugarN = input("¿En donde has estado recientemente?\n")
					c = graph.run("MATCH (n:Pais) WHERE n.nombre = '"+ \
					              lugarN+"' RETURN n").data()
					if (len(l) >0):
					c = Pais()
						c.nombre = lugarN
						graph.pull(c)
						p.yaVisitoP.add(c)
						graph.push(p)
					else:
					print("Ese lugar no esta en la BD :(")
				else:
				print("Ese no es un valor valido")
			elif(des1 =="6"):
			n0 = input("¿Con quien te has peleado, que deseas eliminar de tu lista de amigos?\n")
				amigo = Persona()
				amigo.nombre = n0
				l = graph.run("MATCH (n:Persona) WHERE n.nombre = '"+ \
				              n0+"' RETURN n").data()
				if (len(l) >0):
				graph.pull(amigo)
					p.amigos.remove(amigo)
					print("Listo... \n")
					graph.push(p)
			elif(des1 =="7"):
			sigue = False
				print("Hasta luego!")
			else:
			print("Ese no es un valor valido :(")
	elif(nombre =="X" or "x"):
		sigue0 = False
		print("Adios ")
	else:
	print("Ese nombre no esta registrado :(")
