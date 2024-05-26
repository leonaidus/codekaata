# Supermarket Checkout Process

This Python code implements a supermarket checkout process that calculates the total price of items added to the cart by the customer. The store uses individual letters of the alphabet (A, B, C, and so on) to represent items. Products can be purchased at their individual pricing or at discounted prices when purchased in groups.

## Pricing Rules

Special pricing rules are applied to certain items based on the quantity purchased. Here are some examples of pricing rules:

- **Item A**: Buy three 'A's for $1.30.
- **Item B**: Buy two 'B's for Rs 45.

## Usage

1. Clone this repository or download the source code.
2. Make sure you have Python installed on your system.
3. Run the `main.py` script to test the checkout with custom inputs.
4. Run tests using `pytest`.

```python
# Example usage
cart = Cart()

# Scan items
cart.add('B')
cart.add('A')
cart.add('B')

# Calculate total
total = cart.total
print("Total order pricing:", total)
```

## Docker

A Dockerfile is provided in case you want to run the code within a Docker container. Follow these steps:

1. Build the Docker image:
    ```
    docker build -t supermarket-checkout .
    ```

2. Run the Docker container:
    ```
    docker run -it --rm supermarket-checkout /bin/bash
    ```

3. Run python script to test for custom inputs
   ```
   python main.py
   ```

## Customize Pricing Rules

You can customize the pricing rules for different items by modifying the `PRICE_MAP` dictionary in the code present in `constants.py`. Each item should have its own pricing rule function defined.

Feel free to extend or modify the code according to your specific requirements. Happy shopping! 🛒🎉
```