from Offer import Offer
from constants import ValueErrorMessages


class TestOffer:

	def test_quantity_for_invalid_values(self):
		try:
			offer = Offer(quantity=-5, price=150)
		except ValueError as e:
			assert str(e) == ValueErrorMessages.quantity
		try:
			offer = Offer(quantity="-5", price=150)
		except ValueError:
			assert True
		try:
			offer = Offer(quantity="ab", price=150)
		except ValueError:
			assert True

	def test_quantity_for_valid_values(self):
		offer = Offer(quantity=5, price=150)
		assert offer.quantity == 5

	def test_price_for_invalid_values(self):
		try:
			offer = Offer(quantity=5, price=-150)
		except ValueError as e:
			assert str(e) == ValueErrorMessages.price
		try:
			offer = Offer(quantity=5, price="-150")
		except ValueError:
			assert True
		try:
			offer = Offer(quantity=5, price="abc")
		except ValueError:
			assert True

	def test_price_for_valid_values(self):
		offer = Offer(quantity=5, price=150)
		assert offer.price == 150
