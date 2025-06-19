from main import MainFunction

main=MainFunction()
print(main.t)

class TicketPrinter:
    def __init__(self):
        self.hi=3
    def ticket_booking(self):
        re_book=int(input("\n1.book more\n2.get ticket\n3.Exit \nEnter the option:"))
        if re_book==2:
           A=len(self.general_booked_ceat)
        #    print(Mov.ticket_variable[0])
           print("\n you have booked ",A," seats")
           print(" 1 VIP = 250\n",A,"VIP = ",A*250)
           print("Thankyou.....\n\n")
        elif re_book==1:
            print("You can book more seat")
            self.book_more_seats(self.general_empty_ceat_list,0,70)   
        else:
            return  
        
        