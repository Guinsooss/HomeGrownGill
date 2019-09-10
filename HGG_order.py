menu = {
    # item categories
    'fruits': {
        # items inside each category
        'apples': {
            # the price of the item
            'price': 3
        },
        'oranges': {
            'price': 3
        },
        'watermelon': {
            'price': 1.50
        }
    },

    'vegetables': {
        'potato': {
            'price': 1
        },
        'cabbage': {
            'price': 2.50
        },
        'carrot': {
            'price': 1.50
        },
    },

    'dairy': {
        'milk': {
            'price': 2.00
        },

    },

    'nuts': {
        'peanuts:': {
            'price': 2.50
        },
        'almond:': {
            'price': 2.50
        },
        'pistachio': {
            'price': 2.50
        }
    },
    'jams': {
        'raspberry jam': {
            'price': 4
        },
        'blackberry jam': {
            'price': 4
        },

    },

    'juices': {
        'apple juice': {
            'price': 3
        },
        'orange juice': {
            'price': 4
        }
    }
}
# creating an empty dictionary for the order
order = {

}


# printing the whole menu out with updated items
print("This is the menu, please select items off of here. ")


# creating a function to print a dictionary
def print_dict(dictionary):
    # looking at the different keys in the dictionary
    for key, dictionary in dictionary.items():
        print()
        # printing the key out
        print(key.capitalize())
        print()
        # printing item and its price
        for attribute, value in dictionary.items():
            print('{} : ${}'.format(attribute.capitalize(), value['price']))


# printing function out with menu dictionary
print_dict(menu)
print()


# creating the ordering system
def ordering(menu_dict, order_dict):
    # creating ordering loop
    ord = True
    while ord:
        try:
            try:
                # asking them which item they would like to purchase
                order_item = input("What item would you like to purchase from the menu? ").lower()
                # asking how many items they would like to purchase
                order_quantity = int(input("How many would you like to purchase? "))
                # print("printing",menu_dict.items()

                # if the item is already in the order
                if order_item in order_dict:
                    # add the quantity in the above statement to the quantity already in the order
                    order_dict[order_item]['quantity'] = order_dict[order_item]['quantity'] + order_quantity
                    # print("hi")
                    # break the loop
                    break
                else:
                    for category, value in menu_dict.items():
                       # print("sd",category)
                       # print("fh",value)
                       #  print("printing",list(value.keys()))
                       # if the order item is is in the dictionary
                        if order_item in list(value.keys()):
                            # print("Hola")
                            # add the order item and quantity to the empty dictionary
                            order_dict[order_item] = {'price for each item': value[order_item]['price'], 'quantity': order_quantity}
                            ord = False
                            break
                # if the item is not in the menu
                if order_item not in order_dict:
                    # print error message
                    print("Please enter in a correct item. ")
            except KeyError:
                print("Please enter in a correct item. ")
        except ValueError:
            print("Please enter in a quantity above 0 and a whole number. ")


ordering(menu, order)

# repeat ordering loop
repeat_order = True
while repeat_order:
    # asking if they want to repeat their order
    r_order = input("Would you like to add another item to your order? (Yes or no) ").lower()
    # if yes
    if r_order == "yes":
        # redo ordering function
        ordering(menu, order)
    # if no
    elif r_order == "no":
        # break the loop
        repeat_order = False
    # if input was not yes or no
    else:
        # ask them to redo
        print("Please enter yes or no.")


# for key, order in order.items():
print()
print("Your order is:")
#print(key.capitalize())
for attribute, value in order.items():
    # print item
    print(attribute.capitalize())
    # print the individual price for the items
    print("Price per item: ${}".format(value['price for each item']))
    # print the quantity they selected
    print("Quantity: {}".format(value['quantity']))
    print()


# print(order)
