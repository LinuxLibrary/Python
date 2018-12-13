#!/usr/bin/python

# FUNCTIONS
def print_menu(menu):
	for name, price in menu.items():
		print(name, ': $', format(price, '.2f'), sep='')
		

def get_orders(menu):
	orders = []
	order = input("what would you like to order? (Q to Quit)")
	
	while (order.upper() != 'Q'):
		# Find the order
		FOUND = menu.get(order)
		if FOUND:
			orders.append(order)
		else:
			print("Menu item doesn't exist")
			
		order = input("Anything else? (Q to Quit)")
		
	return orders
	

def bill_total(orders, menu):
	total = 0
	
	for order in orders:
		total += menu[order]
		
	return total
	
	
def main():
	menu = {'Knackered Spam': 4.0, 'Pip Pip Spam': 3.0, 'Cheerio Spam': 2.0, 'Cheeky Spam': 1.0}
	print_menu(menu)
	orders = get_order(menu)
	total = bill_total(orders, menu)
	print("You ordered:", order,
		  "Your total is: $", format(total, '.2f'), sep='')
	
	
main()