#!/usr/bin/env python

from secuenciaordenada import SecuenciaOrdenada
import random
import unittest

class TestSecuenciaOrdenada(unittest.TestCase):

	def test_mismos_elementos(self):
		"""Testea que la SecuenciaOrdenada tenga los mismos elementos que se usaron para construirla"""
		s0 = [random.randint(0, 50) for x in range(0, 10)]
		s1 = SecuenciaOrdenada(s0)

		self.assertItemsEqual(s0, s1.secuencia())

	def test_aliasing(self):
		"""Testea problemas de aliasing"""
		s0 = range(0, 10)
		s1 = SecuenciaOrdenada(s0)
		random.shuffle(s0)

		for i in range(0, s1.longitud()-1):
			self.assertLessEqual(s1.obtener(i), s1.obtener(i+1))

	def test_borrar_elementos(self):
		"""Testea la consistencia del metodo borrar"""
		s = SecuenciaOrdenada(range(0, 10))

		self.assertEqual(s.longitud(), 10)

		longitud_vieja = s.longitud()
		s.eliminar(4)

		self.assertEqual(s.longitud(), longitud_vieja-1)

		ultimo_viejo = s.ultimo()
		primero_viejo = s.primero()
		s.eliminar(s.longitud()-1)

		self.assertNotEqual(s.ultimo(), ultimo_viejo)
		self.assertEqual(s.primero(), primero_viejo)

if __name__ == "__main__":
	unittest.main()
