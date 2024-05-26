from Cart import Cart

if __name__ == '__main__':
	a = input()
	cart = Cart()
	for i in a:
		cart.add(i)

	print(cart.total)
