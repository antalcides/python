class SecuenciaOrdenada:
	"""SecuenciaOrdenada: secuencia que mantiene sus elementos en orden"""

	def __init__(self, s):
		self.s = s
		self.s.sort()

	def primero(self):
		return self.obtener(0)

	def ultimo(self):
		return self.obtener(self.longitud()-1)

	def obtener(self, n):
		return self.s[n]

	def insertar(self, e):
		self.s.append(e)
		self.s.sort()

	def eliminar(self, n):
		del self.s[n]
	
	def longitud(self):
		return len(self.s)

	def secuencia(self):
		return self.s

	def vacio(self):
		return self.longitud() == 0
