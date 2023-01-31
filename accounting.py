melon_cost = 1.00

"""Create a function to tell if customer over or underpaid"""
def correct_payment(the_file):
    for line in the_file:

        """Assign variable names to varibles"""
        words = line.split('|')
        name = words[1]
        melon_quantity = int(words[2])
        price_paid = float(words[3])

        
        """Find correct price with melon price and melon quantity"""
        correct_price = (melon_cost * melon_quantity)

        """Print statement if price paid doesn't equal the correct price """
        if price_paid != correct_price:
            print(f'{name} paid ${price_paid},' 
            f' expected ${correct_price}')

correct_payment(open("customer-orders.txt"))