order = {'apples': {'price for each item': 3, 'quantity': 20}, 'oranges': {'price for each item': 3, 'quantity': 2}, 'watermelon': {'price for each item': 1.5, 'quantity': 2}, 'potato': {'price for each item': 1, 'quantity': 2}, 'raspberry jam': {'price for each item': 4, 'quantity': 2}, 'apple juice': {'price for each item': 3, 'quantity': 5}}


# creating delete item function
def delete(order_dict):
    # creating a loop
    delete = True
    while delete:
        try:
            try:
                # asking what item they would like to delete / remove quantity
                order_item = input("What item would you like to delete/ lower the quantity of from your order? ").lower()
                # asking the quantity of the items they would like to remove
                order_del_quantity = int(input("How many would you like to delete off of your order? "))
                # print("printing",menu_dict.items())
                # if the quantity to remove is larger than the quantity available to be removed
                if order_del_quantity <= 0:
                    print("Please enter a number larger than 0. ")
                else:
                    # if the item is in the order
                    if order_item in order_dict:
                        # remove the quantity
                        order_dict[order_item]['quantity'] = order_dict[order_item]['quantity'] - order_del_quantity
                        # print("hi")
                        # stop the loop
                        delete = False
                    # if the quantity goes below 0 or at 0
                    if order_dict[order_item]['quantity'] - order_del_quantity == 0 or order_dict[order_item]['quantity'] - order_del_quantity < 0:
                        # remove from the order
                        order_dict.pop(order_item)
                        # print("asdfsda")
            except KeyError:
                print("Please enter in a correct item. ")
        except ValueError:
            print("Please enter in a quantity above 0 and a whole number. ")
    # print out messages saying the amount deleted and what item it was from
    print("{} {} have been removed from your order.".format(order_del_quantity, order_item))
    print()
    # re-printing order
    print("Your new order is:")
    for attribute, value in order.items():
        print(attribute.capitalize())
        print("Quantity: {}".format(value['quantity']))
        print()


# loop for re-running the function
option = input("Would you like to delete an item off of your order? ")
if option == 'yes':
    delete(order)
    delete_loop = True
    while delete_loop:
        answer = input("Would you like to delete another item.").lower()
        if answer == "yes":
            delete(order)
        elif answer == "no":
            delete_loop = False
        else:
            print("Print please enter yes or no")
elif option == "no":
    print("thanks")




