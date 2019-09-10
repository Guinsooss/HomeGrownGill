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
        'raspberry': {
            'price': 4
        },
        'blackberry': {
            'price': 4
        },

    },

    'juices': {
        'apple': {
            'price': 3
        },
        'orange': {
            'price': 4
        }
    }
}

# print(menu)


# creating a function for the questions
def add(dict, amount):
    # creating the loop
    loop = True
    while loop:
        try:
            try:
                # asking which item type the item will go under
                item_type = input('What item type would you like to add (fruits, vegetables, dairy, nuts, jams, juices)? ').lower()
                # asking what the item will be
                item = input('What item would you like to add? ').lower()
                # asking what the item's price will be
                cost = str(input('What price would you like {} to cost? '.format(item)))
                # converting the cost into a float
                cost = float(cost)
                # adding the item and its cost to the dictionary
                dict[item_type][item] = {amount:cost}
                loop = False
                print('{} has been added for ${}'.format(item.capitalize(), cost))
                # validation if the key is incorrect
            except KeyError:
                print('Please select a correct item type. ')
        # making sure that the price is a number
        except ValueError:
            print('Please enter a price with numerical values and above $0. ')


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


# printing the whole menu out with updated items
def print_dict(dictionary):
    print()
    print('The new menu is: ')
    for key, dictionary in dictionary.items():
        print()
        print(key.capitalize())
        print()
        for attribute, value in dictionary.items():
            print('{} : ${}'.format(attribute.capitalize(), value['price']))


print_dict(menu)