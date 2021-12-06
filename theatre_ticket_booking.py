seat = "S"
seat_column = int(input("Required columns : "))
seat_row = int(input("Required rows    : "))
total_seats = seat_column * seat_row
seat_generator = seat*total_seats
seat_generator = list(seat_generator)
customer_details = {}   #empty dictonary to store customer details

def book_ticket():
    y = 0
    z = 1
    for i in seat_generator:
        if y != seat_column:
            if z < 10:    #To print prifx 0 for single numerical values
                print(0,end='')
            print(z,i, end="  ")   #To print seats in a given order
            y = y + 1
            z = z + 1
        else:
            y = 1
            print()
            if z < 10:
                print(0,end='')
            print(z,i, end="  ")
            z = z + 1

def income():
    fill = 0
    for i in seat_generator:
        if i == "B":
            fill = fill + 1   #To calculate income
    income = fill * 85
    print("Total seats filled :",fill)
    print("Overall income     :",income)

while True:
    print()
    print("<----------------Global Theater Welcome's You------------------->")
    print("Choose your Action:\nShow Available seats------->(1)\nBook a seat---------------->(2)\nShow Income---------------->(3)\nShow seat details---------->(4)\nExit----------------------->(5)")
    user_input = int(input("Your Action : "))

    if user_input == 1:
        book_ticket()

    elif user_input == 2:
        book = int(input("Choose seat number : "))
        if book < total_seats:
            if seat_generator[book-1] != "B":   #Check seat is available or not
                seat_generator[book-1] = "B"
                seat_no = book
                name = str(input("Your Name          : "))
                age = str(input("Your Age           : "))
                gender = str(input("Your Gender        : "))
                customer_details[seat_no] = [name,age,gender]
                print("Booking Successful")
            else:
                print("Already Booked")
        else:
            print("Invaild Seat Number")

    elif user_input == 3:
        income()

    elif user_input == 4:
        try:
            required_seat = int(input("Seat Number : "))
            details_list = customer_details[required_seat]   #To print seat details
            print("Name        :",details_list[0])
            print("Age         :",details_list[1])
            print("Gender      :",details_list[2])
        except:
            print("Given seat number",required_seat,"is not booked any one")
        
    elif user_input == 5:
        break

    else:
        print("Invalid Input")

