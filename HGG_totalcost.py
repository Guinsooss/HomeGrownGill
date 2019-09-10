order = {'apples': {'price for each item': 3, 'quantity': 20}, 'oranges': {'price for each item': 3, 'quantity': 2}, 'watermelon': {'price for each item': 1.5, 'quantity': 2}, 'potato': {'price for each item': 1, 'quantity': 2}, 'raspberry jam': {'price for each item': 4, 'quantity': 2}, 'apple juice': {'price for each item': 3, 'quantity': 5}}

def total_cost(order_dict):
    # set the price to 0
    price = 0
    # for all items in the order dictionary
    for order_item in order_dict:
        # sets up total cost
        price2 = price
        # calculating the price per item
        price = (order_dict[order_item]['quantity'] * order_dict[order_item]['price for each item'])
        print(order_item.capitalize())
        # printing out the individual total item price

        print('Total item price is ${}'.format(price))
        print()
        # add the total individual item prices together
        price = price + price2
    print()
    # printing out total price
    print('Total price for all of your items is ${}'.format(price))


total_cost(order)