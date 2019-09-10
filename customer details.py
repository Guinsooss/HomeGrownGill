# Creating function for customer details
def customer_details():
    # phone_num is for loop within function
    phone_num = True
    # asking for name
    name = str(input("What is your name? "))
    # asking for address
    address = input("What is your home address? ")
    while phone_num:
        # asking for a phone number that is a string
        phone_number = str(input("What is your phone number "))
        try:
            # checking and converting the string into a integer that is above 0
            if int(phone_number) <0:
                print("A phone number needs to have numerical values above 0. ")
                continue
            else:
                # ending loop if phone number is greater than 0
                phone_num = False
                return name, address, phone_number

        except ValueError:
        # printing an error
            print("Please enter a valid phone number. ")


# returning inputs to the rest of the code
name, address, phone_number = customer_details()
print(name, address, phone_number)



