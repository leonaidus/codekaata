from constants import ValueErrorMessages


class Offer:
	def __init__(self, quantity: int, price: float):
		self.quantity = quantity
		self.price = price

	@property
	def quantity(self) -> int:
		return self._quantity

	@quantity.setter
	def quantity(self, quantity: int):
		if type(quantity) is not int:
			quantity = int(quantity)
		if quantity <= 0:
			raise ValueError(ValueErrorMessages.quantity)
		self._quantity = quantity

	@property
	def price(self) -> float:
		return self._price

	@price.setter
	def price(self, value: float):
		if type(value) is not float:
			value = float(value)
		if value <= 0:
			raise ValueError(ValueErrorMessages.price)
		self._price = value
