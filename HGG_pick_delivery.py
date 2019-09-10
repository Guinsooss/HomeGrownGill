def pickup_delivery():
    # loop for repeating question if needed
    del_pick = True
    while del_pick:
        # asking the user if they want delivery or pick up
        option = input("Would you like your order to be delivered or ready for pickup (Delivery is $3 Extra)? ").lower()
        # if they pick delivery
        if option == "delivery" or option == "d":
            # ask for delivery address
            delivery_address = input("What is your delivery address? ")
            # ask if the input delivery was correct
            correct = input("Is this the correct address, {} (Yes or No)? ".format(delivery_address)).lower()
            # if it is correct
            if correct == "yes":
                # print the delivery address
                print("Your order will be sent to {}.".format(delivery_address))
                break
            else:
                continue
        # if the user picked pick up
        if option == "pick up" or option == "pickup" or option == "p":
            # tell them when it will be ready to pick up
            print("Your order will be ready to pick up within 1 to 2 business days. ")
            # making it so the loop does not continue
            del_pick = False


pickup_delivery()




