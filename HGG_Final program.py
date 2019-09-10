import math

over_all_loop = True
repeat_loop = True


menu = {
    # item categories
    'fruits': {
        # items inside each category
        'apples': {
            # the price of the item
            'price': 2
        },
        'oranges': {
            'price': 2
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
        'peanuts': {
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
        'raspberry': {
            'price': 4
        },
        'blackberry': {
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


order = {

}


# asking for the customers details
def customer_details():
    # phone_num is for loop within function
    name_loop = True
    global name_input

    while name_loop:
        # asking for name
        name_input = str(input("What is your name? "))
        if not name_input.split():
            print("Please input a name.")
        else:
            name_loop = False
    # asking for address
    # address_input = input("What is your home address? ")
    phone_num = True
    while phone_num:
        # asking for a phone number that is a string
        phone_number_input = str(input("What is your phone number "))
        try:
            # checking and converting the string into a integer that is above 0
            if int(phone_number_input) <= 0:
                print("A phone number needs to have numerical values above 0. ")
                continue
            else:
                # ending loop if phone number is greater than 0
                phone_num = False
                return name_input, phone_number_input

        except ValueError:
            # printing an error
            print("Please enter a valid phone number. ")


# creating a function for the questions
def add(dictionary, amount):
    # creating the loop
    loop = True
    while loop:
        try:
            try:
                # asking which item type the item will go under
                item_type = input('What item type would you like to add (fruits, vegetables, dairy, nuts,'
                                  ' jams, juices)? (To cancel command, type cancel). ').lower()
                global item
                # if the user wants to cancel the adding function
                if item_type == "cancel":
                    # loop stops and returns to menu
                    loop = False
                    print()
                # if cancel is not entered
                elif not item_type.split():
                    print("Please enter a category.")
                else:
                    item_loop = True
                    while item_loop:
                        # asking what the item will be
                        item = input('What item would you like to add? ').lower()
                        if not item.split():
                            print("Please enter a item in.")
                        else:
                            item_loop = False
                    # asking what the item's price will be
                    cost = float(input('What price would you like {} to cost? '.format(item)))
                    if cost > 0:
                        # converting the cost into a float
                        # adding the item and its cost to the dictionary
                        dictionary[item_type][item] = {amount: cost}
                        loop = False
                        print('{} has been added for ${}'.format(item.capitalize(), cost))
                    if cost <= 0:
                        print("Please enter a value above $0.")
            # validation if the key is incorrect
            except KeyError:
                print('Please select a correct item type. ')
        # making sure that the price is a number
        except ValueError:
            print('Please enter a price with numerical values and above $0. ')


# creating the ordering system
def ordering(menu_dict, order_dict):
    # creating ordering loop
    order_loop = True
    while order_loop:
        try:
            try:
                # asking them which item they would like to purchase
                order_item = input("What item would you like to purchase from the menu? (If you want to go back, type"
                                   " cancel) ").lower()
                # if the user wants to cancel the ordering function
                if order_item == "cancel":
                    # the loops is false so it will return to the main menu and stop looping
                    order_loop = False
                    print()
                # if the user doesn't type cancel
                else:
                    # asking how many items they would like to purchase
                    order_quantity = int(input("How many would you like to purchase? "))
                    if order_quantity < 1:
                        print("You can not order 0 or less items")
                    else:
                        # print("printing",menu_dict.items())
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
                                    # print("hello")
                                    # add the order item and quantity to the empty dictionary
                                    order_dict[order_item] = {'price for each item': value[order_item]['price'], 'quantity': order_quantity}
                                    order_loop = False
                                    print("{} {}(s) have been added to your order. ".format(order_quantity,
                                                                                            order_item.title()))
                                    break
                        # if the item is not in the menu
                        if order_item not in order_dict:
                            # print error message
                            print("Please enter in a correct item. ")
            except KeyError:
                print("Please enter in a correct item. ")
        except ValueError:
            print("Please enter in a quantity above 0 and a whole number. ")
        print()


def total_cost(order_dict):
    # set the price to 0
    price = 0
    print("Your order is:")
    print()
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
    return price


# creating delete item function
def delete(order_dict):
    # creating a loop
    while delete:
        try:
            try:
                # asking what item they would like to delete / remove quantity
                order_item_del = input("What item would you like to delete/ lower the quantity of from your "
                                       "order? (If you want to exit the current process, type cancel)").lower()
                # if the user wants to cancel the delete function
                if order_item_del == "cancel":
                    # breaks the loop/function
                    break
                else:
                    # asking the quantity of the items they would like to remove
                    order_del_quantity = int(input("How many would you like to delete off of your order? "))
                    # print("printing",menu_dict.items())
                    # if the quantity to remove is larger than the quantity available to be removed
                    if order_del_quantity <= 0:
                        print("Please enter a number larger than 0. ")
                    else:
                        # if the item is in the order
                        if order_item_del in order_dict:
                            # remove the quantity
                            if order_dict[order_item_del]['quantity'] - order_del_quantity > 0:
                                order_dict[order_item_del]['quantity'] = order_dict[order_item_del]['quantity'] - order_del_quantity
                                print("{} {} have been removed from your order.".format(order_del_quantity, order_item_del))
                                print()
                                # re-printing order
                                print("Your new order is:")
                                for attribute, value in order.items():
                                    print(attribute.capitalize())
                                    print("Quantity: {}".format(value['quantity']))
                                    print()
                                # print("hi")
                                # stop the loop
                                break
                            # if the quantity goes below 0 or at 0
                            elif order_dict[order_item_del]['quantity'] - order_del_quantity == 0 or order_dict[order_item_del]['quantity'] - order_del_quantity < 0:
                                # remove from the order
                                del order_dict[order_item_del]
                                print()
                                print("{} has been removed from your order.".format(order_item_del.title()))
                                break
            except KeyError:
                print("Please enter in a correct item. ")
        except ValueError:
            print("Please enter in a quantity above 0 and a whole number. ")
    # print out messages saying the amount deleted and what item it was from


# creating box size function                                                                         
def box(order_dict, price):
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
    pick_del_loop = True
    # checking the input
    while pick_del_loop:
        paper_bags = input("Would you like to use paper bags ($1 extra) or in boxes? ").lower()
        if paper_bags == "yes" or paper_bags == "p" or paper_bags == "paper" or paper_bags == "paper bags" \
                or paper_bags == "bags" or paper_bags == "paper bag":
            print("Your order will be packaged in paper bags.")
            bag_price = price + 1
            return bag_price
        elif paper_bags == "box" or paper_bags == "boxes":
            # if the total quantity is less than 10
            if total_quantity < 10:
                # divide by 5
                box_amount = total_quantity / 5
                # round the number up
                box_amount = math.ceil(box_amount)
                print("{} small box(s) will store all your items.".format(box_amount))
            # if the total quantity is greater than 10 but less than 30
            elif 10 < total_quantity < 30:
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
            return price
        else:
            print("Please input paper bags or boxes.")


# printing the selected dictionary
def print_dict(dictionary):
    print()
    print('The menu is: ')
    # looks through the keys in the dictionary and the items
    for key, dictionary in dictionary.items():
        print()
        # prints the key
        print(key.capitalize())
        print()
        for attribute, value in dictionary.items():
            # prints both the item inside the key and the price
            print('{} : ${}'.format(attribute.capitalize(), value['price']))


# creating pick up or delivery function
def pickup_delivery(price):
    # loop for repeating question if needed
    del_pick = True
    while del_pick:
        # asking the user if they want delivery or pick up
        pick_del = input("Would you like your order to be delivered or ready for pickup (Delivery is $3 Extra)? ").lower()
        # if they pick delivery
        if pick_del == "delivery" or pick_del == "delivered" or pick_del == "d":
            # ask for delivery address
            delivery_address = input("What is your delivery address? ")
            # ask if the input delivery was correct
            correct_loop = True
            while correct_loop:
                correct = input("Is this the correct address, {} (Yes or No)? ".format(delivery_address)).lower()
                # if it is correct
                if correct == "yes" or correct == "y":
                    # print the delivery address
                    print("Your order will be sent to {} within 2-3 working days.".format(delivery_address))
                    new_price = price + 3
                    return new_price
                elif correct == "no" or correct == "n":
                    correct_loop = False
                else:
                    print("Please input yes or no. ")
        # if the user picked pick up
        elif pick_del == "pick up" or pick_del == "pickup" or pick_del == "p":
            # tell them when it will be ready to pick up
            print("We will call you on {} when your order is ready to pick up. ".format(phone_number))
            # making it so the loop does not continue
            return price
        else:
            print("Please type pick up or delivery.")


while repeat_loop:
    over_all_loop = True
    name, phone_number = customer_details()
    order.clear()
    print()
    print("Welcome {} to Home Grown Gill's store!".format(name.title()))

    while over_all_loop:
        print()
        option = input('''
        1. (Owner Only) Add an item to the ordering menu (Owner Only)
        2. View the menu 
        3. Add an item to your order
        4. View the Total cost of your order
        5. View order
        6. Delete or lower the quantity of an item from your order
        7. Complete your order and chose Delivery/pick up options
        8. Cancel order
        
        Please enter in 1,2,3,4,5,6,7 or 8. ''')

        if option == "1":
            add(menu, 'price')
            """
            # setting up a loop
            repeat_loop = True
            while repeat_loop:
                add(menu, 'price')
                # asking if they want to repeat the function
                repeat = input("Would you like to add another item to the menu? (Yes or no) ").lower()
                if repeat == "yes":
                    add(menu, 'price')
                elif repeat == "no":
                    repeat_loop = False
                else:
                    # stopping the loop
                    print("Please enter yes or no. ")
            print_dict(menu)
            """
        # prints the menu
        elif option == "2":
            # prints the menu
            print_dict(menu)

        elif option == "3":
            # calling the menu
            print_dict(menu)
            # calling the ordering function
            print()
            ordering(menu, order)
            """
            #repeat ordering loop
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
             
            for key, order in order.items():"""

        elif option == "4":
            # calls the total_cost function
            total_cost(order)

        elif option == "5":
            print()
            print("Your order is:")
            # print(key.capitalize())
            for attribute, value in order.items():
                # print item
                print(attribute.capitalize())
                # print the individual price for the items
                print("Price per item: ${}".format(value['price for each item']))
                # print the quantity they selected
                print("Quantity: {}".format(value['quantity']))
                print()

        elif option == "6":
            delete(order)
            """
            ask the user if they are sure about deleting an item
            option = input("Would you like to delete an item off of your order? ")
            if answer is yes
            if option == 'yes':
                call the delete function
                creating a loop for the delete function
                delete_loop = True
                while delete_loop:
                    print()
                    ask if they want to delete another item
                    answer = input("Would you like to delete another item.").lower()
                    print()
                    if answer is yes
                    if answer == "yes":
                        call the delete function again
                    if answer is no
                    elif answer == "no":
                        make the loop equal to false
                        delete_loop = False
                    else:
                        ask the user to enter yes or no
                        print("Print please enter yes or no")
            elif option == "no":
                continue"""

        elif option == "7":
            print()
            order_price = total_cost(order)
            if order_price == 0:
                print("You need to order items to complete an order! ")
            else:
                box_price = box(order, order_price)
                final_price = pickup_delivery(box_price)
                print()
                print("Your order is:")
                # print(key.capitalize())
                for attribute, value in order.items():
                    # print item
                    print(attribute.capitalize())
                    # print the individual price for the items
                    print("Price per item: ${}".format(value['price for each item']))
                    # print the quantity they selected
                    print("Quantity: {}".format(value['quantity']))
                    print()
                print('The total cost of your order is ${}, this includes delivery and paper bags if selected. '.format(final_price))
                print()
                print("Thanks for shopping {} at Home Grown Gill's, please come again another time.".format(name))
                over_all_loop = False
                repeat_input_loop = True
                while repeat_input_loop:
                    repeat = input("Would you like to order again? (Yes or No)")
                    if repeat == "y" or repeat == "yes":
                        repeat_input_loop = False
                        print()
                        continue
                    elif repeat == "n" or repeat == "no":
                        repeat_input_loop = False
                        over_all_loop = False
                        repeat_loop = False
                    else:
                        print("Please enter yes or no.")

        elif option == "8":
            cancel_loop = True
            cancel = 0
            while cancel_loop:
                cancel = input("Are you sure you would like to cancel your order? ")
                if cancel == "yes" or cancel == "y":
                    cancel_loop = False

                    over_all_loop = False
                    repeat2loop = True
                    while repeat2loop:
                        repeat2 = input("Would you like to order again? (Yes or No)")
                        if repeat2 == "y" or repeat2 == "yes":
                            print()
                            repeat2loop = False
                            continue
                        elif repeat2 == "n" or repeat2 == "no":
                            repeat2loop = False
                            over_all_loop = False
                            repeat_loop = False
                        else:
                            print("Please enter yes or no.")

                elif cancel == "no" or cancel == "n":
                    cancel_loop = False
                else:
                    print("Please enter yes or no.")
            # if cancel == "yes" or cancel == "y":
            #     break

        else:
            print()
            print("Please enter in a correct option.")