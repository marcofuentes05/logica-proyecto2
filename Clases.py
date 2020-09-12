from py2neo.ogm import *
from py2neo import *

class Persona(GraphObject):
	__primarykey__ = "nombre"

	nombre = Property()

	amigos = Related("Persona", "amigos")
	likes = Related("Atributo", "likes")
	yaVisito = Related("Ciudad", "yaVisito")
	yaVisitoP = Related("Pais", "yaVisitoP")


class Ciudad (GraphObject):
	__primarykey__ = "nombre"
	nombre = Property()

	def __init__(self):
	self.contador = 0

	def agregarC(self, numero):
	self.contador = contador + int(numero)


class Pais (GraphObject):
	__primarykey__ = "nombre"
	nombre = Property()

	def __init__(self):
	self.contador = 0

	def agregarC(self, numero):
	self.contador = self.contador + int(numero)


class Atributo(GraphObject):
	__primarykey__ = "cualidad"

	cualidad = Property()
	es = Related("Ciudad", "es")
	esP = Related("Pais", "esP")


class Lugar(object):
	def __init__(self, nombre):
	self.nombre = nombre
	self.contador = 0

	def sumar(self, numero):
	self.contador = self.contador + numero