from Offer import Offer
from constants import PRICE_MAP, ValueErrorMessages


class ProductDoesNotExist(Exception):
	pass


class Product:
	def __init__(self, name: str, price: float or None = None, offer: Offer or None = None):
		self.name = name
		# Price Feeder logic below from constants.
		# Below can be also fed through database or excel.
		if price is None:
			try:
				self.price = PRICE_MAP[name]['price']
			except KeyError:
				raise ProductDoesNotExist(name + ' Product does not exist')
			if 'offer' in PRICE_MAP[name]:
				offer = Offer(quantity=PRICE_MAP[name]['offer']['quantity'], price=PRICE_MAP[name]['offer']['price'])
		else:
			self.price = price
		self.offer = offer

	@property
	def name(self) -> str:
		return self._name

	@name.setter
	def name(self, value: str):
		if not isinstance(value, str):
			raise ValueError(ValueErrorMessages.name)
		self._name = value

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

	@property
	def offer(self) -> Offer or None:
		return self._offer

	@offer.setter
	def offer(self, value: Offer or None):
		self._offer = value
