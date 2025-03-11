# Seats alignment  VIP=500(1-20), PREMIUM=250(21-50), REGULAR=150(51-100)
def seat_arrangement(type_of_seat):
    if type_of_seat == 1:
        print("You selected VIP seat")
        seats1 = list(range(1, 21))
        print("Remaining seats are", seats1)
        length_of_seats1 = len(seats1)

        no_booking = int(input("Enter the number of seats to book: "))  # Taking input properly

        for no_of_booking in range(1, no_booking + 1):  # Loop for seat booking
            while True:
                t = int(input(f"Enter the {no_of_booking} seat number: "))
                if t<1  or  t>21:
                    print("this type of seats are not available in VIP cabin")
                elif t not in seats1:
                    print("Seats have been already booked")
                else:
                    # Seat booking message
                    print(f"{no_of_booking}) Seat number {t} is booked for you")
                    seats1.remove(t)
                    print("Remaining seats are", seats1)
                    length_of_seats1 -= 1
                    break  # Exit while loop once seat is booked

    elif type_of_seat == 2:
        print("You selected PREMIUM seat")
        seats2 = list(range(21, 51))  # Fixed range (was 20-50, now corrected to 21-50)
        print("Remaining seats are", seats2)
        length_of_seats2 = len(seats2)
        
        no_booking = int(input("Enter the number of seats to book: "))  # Taking input properly

        for no_of_booking in range(1, no_booking + 1):  # Loop for seat booking
            while True:
                t = int(input(f"Enter the {no_of_booking} seat number: "))
                if t<21  or  t>50:
                    print("this type of seats are not available in PREMIUM cabin")

                elif t not in seats2:
                    print("Seats have been already booked")
                else:
                    # Seat booking message
                    print(f"{no_of_booking}) Seat number {t} is booked for you")
                    seats2.remove(t)
                    print("Remaining seats are", seats2)
                    length_of_seats2 -= 1
                    break  # Exit while loop once seat is booked

    elif type_of_seat == 3:
        print("You selected REGULAR seat")
        seats3 = list(range(51, 101))
        print("Remaining seats are", seats3)
        length_of_seats3 = len(seats3)
        
        no_booking = int(input("Enter the number of seats to book: "))  # Taking input properly

        for no_of_booking in range(1, no_booking + 1):  # Loop for seat booking
            while True:
                t = int(input(f"Enter the {no_of_booking} seat number: "))
                if t<51  or  t>100:
                    print("this type of seats are not available in REGULAR cabin")

                elif t not in seats3:
                    print("Seats have been already booked")
                else:
                    # Seat booking message
                    print(f"{no_of_booking}) Seat number {t} is booked for you")
                    seats3.remove(t)
                    print("Remaining seats are", seats3)
                    length_of_seats3 -= 1
                    break  # Exit while loop once seat is booked


print("This is the Seating arrangement")
print("""
             1   2   3   4   5   6   7   8   9  10  
          A [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]  
          B [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]  
                            VIP

             1   2   3   4   5   6   7   8   9  10
          C [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]  
          D [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]  
          E [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]
                          PREMIUM

             1   2   3   4   5   6   7   8   9  10
          F [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]  
          G [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]  
          H [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]  
          I [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]  
          J [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] 
                          REGULAR 
""")

type_of_seat = int(input("1 is VIP seat of 500 Rs:\n2 is PREMIUM seat of 250 Rs:\n3 is REGULAR seat of 150 Rs:\n\nEnter your choice: "))

if 1 <= type_of_seat <= 3:
    seat_arrangement(type_of_seat)  # Function call
else:
    print("There is no such option you entered.")



#Timings


#Check availability


#Print ticket

