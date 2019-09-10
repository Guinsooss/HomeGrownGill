import math
order = {'apples': {'price for each item': 3, 'quantity': 20}, 'oranges': {'price for each item': 3, 'quantity': 2}, 'watermelon': {'price for each item': 1.5, 'quantity': 2}, 'potato': {'price for each item': 1, 'quantity': 2}, 'raspberry jam': {'price for each item': 4, 'quantity': 2}, 'apple juice': {'price for each item': 3, 'quantity': 5}}


# creating box size function
def box(order_dict):
    # setting the quantity to 0
    total_quantity = 0
    # for the items and quantities in your order
    for order_item in order_dict:
        # add the total quantity together
        total_quantity1 = order_dict[order_item]['quantity']
        total_quantity = total_quantity + total_quantity1
    print()
    # print out how many items are in your order
    print("You have {} item(s) in your cart.".format(total_quantity))
    # ask if they want paper bags or boxes
    paper_bags = input("Would you like to use paper bags ($1 extra) or different boxes? ").lower()
    # checking the input
    if paper_bags == "yes" or paper_bags == "p" or paper_bags == "paper" or paper_bags == "paper bags":
        print("Your order will be packaged in paper bags.")
    else:
        # if the total quantity is less than 10
        if total_quantity < 10:
            # divide by 5
            box_amount = total_quantity / 5
            # round the number up
            box_amount = math.ceil(box_amount)
            print("{} small box(s) will store all your items.".format(box_amount))
        # if the total quantity is greater than 10 but less than 30
        elif total_quantity > 10 and total_quantity <30:
            # divide by 10
            box_amount = total_quantity / 10
            # round the number up
            box_amount = math.ceil(box_amount)
            print("{} medium box(s) will store all your items.".format(box_amount))
        # if the quantity is above 30
        elif total_quantity > 30:
            # divide by 15
            box_amount = total_quantity / 15
            # round the number up
            box_amount = math.ceil(box_amount)
            print("{} large box(s) will store all your items.".format(box_amount))


box(order)