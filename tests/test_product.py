from Product import Product
from constants import ValueErrorMessages


class TestProduct:

	def test_price_for_invalid_values(self):
		try:
			product = Product(name="A", price=-150)
		except ValueError as e:
			assert str(e) == ValueErrorMessages.price
		try:
			product = Product(name="A", price="-150")
		except ValueError:
			assert True
		try:
			product = Product(name="A", price="abc")
		except ValueError:
			assert True

	def test_price_for_valid_values(self):
		product = Product(name="A", price=150)
		assert product.price == 150
