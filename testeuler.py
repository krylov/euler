import euler
import unittest

class TestDividersFunction(unittest.TestCase):
	def setUp(self):
		pass
		
	def tearDown(self):
		pass
		
	def test_negatives(self):
		d = euler.dividers(-1)
		self.assertEqual(d, {})
		d = euler.dividers(-100)
		self.assertEqual(d, {})
		
	def test_zero(self):
		d = euler.dividers(0)
		self.assertEqual(d, {})
		
	def test_one_two(self):
		d = euler.dividers(1)
		self.assertEqual(d, {1: 1})
		d = euler.dividers(2)
		self.assertEqual(d, {2: 1})

	def test_prime(self):
		d = euler.dividers(7)
		self.assertEqual(d, {7: 1})

	def test_complex(self):
		d = euler.dividers(10)
		self.assertEqual(d, {2: 1, 5: 1})
		d = euler.dividers(12)
		self.assertEqual(d, {2: 2, 3: 1})

	def test_float(self):
		d = euler.dividers(10.1)
		self.assertEqual(d, {})
		d = euler.dividers(10.9)
		self.assertEqual(d, {})

class TestIsPrimeFunction(unittest.TestCase):
	def setUp(self):
		pass
		
	def tearDown(self):
		pass

	def test_zero(self):
		r = euler.is_prime(0)
		self.assertEqual(r, False)
		
	def test_one(self):
		r = euler.is_prime(1)
		self.assertEqual(r, False)
		
	def test_prime(self):
		r = euler.is_prime(7)
		self.assertEqual(r, True)		
		
	def test_complex(self):
		r = euler.is_prime(8)
		self.assertEqual(r, False)				
		
if __name__ == "__main__":
	unittest.main()
	
