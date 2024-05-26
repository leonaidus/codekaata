from Cart import Cart
from constants import PRICE_MAP


class TestCart:

	def test_add(self):
		cart = Cart()
		cart.add("A")
		assert len(cart.products_quantity_map) == 1
		assert cart.products_quantity_map[0][0].name == "A"
		assert cart.products_quantity_map[0][0].price == PRICE_MAP["A"]['price']

	def test_total(self):
		cart = Cart()
		cart.add("A")
		cart.add("B")
		assert cart.total == PRICE_MAP["A"]["price"] + PRICE_MAP["B"]["price"]

	def test_sample_inputs(self):
		cart = Cart()
		samples = ["", "A", "AB", "CDBA", "AA", "AAA", "AAAA", "AAAAA", "AAAAAA", "AAAB", "AAABB", "AAABBD", "DABABA"]
		outputs = [0, 50, 80, 115, 100, 130, 180, 230, 260, 160, 175, 190, 190]
		for idx, i in enumerate(samples):
			cart.products_quantity_map.clear()
			for j in i:
				cart.add(j)
			assert cart.total == outputs[idx]
