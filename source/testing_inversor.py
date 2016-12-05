from inversor import Inversor
import math
import unittest

class TestInversor(unittest.TestCase):

	def test_unidad(self):
		"""Testea que el inverso de la unidad sea la unidad"""
		i = Inversor(1)
		self.assertEqual(i.valor(), 1.0)

	def test_cero(self):
		"""Testea que falle cuando se pide el inverso de cero"""
		self.assertRaises(ZeroDivisionError, Inversor, 0)

	def test_otro(self):
		"""Testea un valor que tiene un inverso distinto de si mismo"""
		i = Inversor(2)
		self.assertEqual(i.valor(), 0.5)

	def test_doble_inversion(self):
		"""Testea que invertir el inverso de un numero de el numero original"""
		i = Inversor(Inversor(math.pi).valor())
		self.assertEqual(i.valor(), math.pi)

if __name__ == "__main__":
	unittest.main()
