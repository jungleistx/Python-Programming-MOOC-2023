from money import Money
import unittest

class TestMoney(unittest.TestCase):

	def setUp(self) -> None:
		self.zero = Money(0, 0)
		self.fifty = Money(2, 50)
		self.five = Money(2, 5)
		self.small = Money(4, 55)
		self.small2 = Money(4, 55)
		self.big = Money(350, 40)
		return super().setUp()

	def tearDown(self) -> None:
		return super().tearDown()

	def test_eq(self):
		self.assertTrue(self.small == self.small2)
		self.assertTrue(self.zero == Money(0, 0))
		self.assertTrue(self.big == Money(350, 40))
		self.assertFalse(self.zero == self.big)
		self.assertFalse(self.fifty == self.five)
		self.assertFalse(self.fifty == Money(1, 40))

	def test_lt(self):
		self.assertTrue(self.zero < self.fifty)
		self.assertTrue(self.five < self.fifty)
		self.assertTrue(self.small < self.big)
		self.assertTrue(self.small < Money(6, 10))
		self.assertFalse(self.big < self.small)
		self.assertFalse(self.five < self.zero)
		self.assertFalse(self.fifty < self.five)
		self.assertFalse(self.fifty < Money(1, 55))

	def test_gt(self):
		self.assertTrue(self.big > self.small)
		self.assertTrue(self.five > self.zero)
		self.assertTrue(self.fifty > self.five)
		self.assertTrue(self.fifty > Money(1, 55))
		self.assertFalse(self.zero > self.fifty)
		self.assertFalse(self.five > self.fifty)
		self.assertFalse(self.small > self.big)
		self.assertFalse(self.small > Money(6, 10))

	def test_ne(self):
		self.assertTrue(self.big != self.small)
		self.assertTrue(self.five != self.zero)
		self.assertTrue(self.fifty != self.five)
		self.assertTrue(self.fifty != Money(1, 55))
		self.assertFalse(self.small != self.small2)
		self.assertFalse(self.zero != Money(0, 0))
		self.assertFalse(self.five != Money(2, 5))

	def test_add(self):
		self.assertEqual(self.five + self.small, Money(6, 60))
		self.assertEqual(self.five + self.big, Money(352, 45))
		self.assertEqual(self.five + self.fifty, self.small)
		self.assertNotEqual(self.zero + self.small, Money(14, 40))
		self.assertNotEqual(self.fifty + self.small, self.small2)

	def test_sub(self):
		self.assertEqual(self.fifty - self.five, Money(0, 45))
		self.assertEqual(self.small - self.fifty, self.five)
		self.assertEqual(self.big - Money(345, 85), self.small)
		self.assertNotEqual(self.big - self.small, Money(14, 40))
		self.assertNotEqual(self.five, Money(1, 15), self.fifty)
		self.assertNotEqual(self.big - self.zero, self.fifty)


if __name__ == "__main__":
	unittest.main()