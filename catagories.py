from movie_name import Movies

obj=Movies()

#  Seats and Categories
"""
VIP      30   250
REGULAR  70   150 
"""


class Ceat:
    def __init__(self):
        self.empty_seat_list=[]
        
    def vip(self):
        print(self.empty_seat_list)
        vip_seat=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,7,28,29,30]
        print(vip_seat)
        no_seats=int(input("Enter the number of seats to book: "))            
        if 0<no_seats<30:
            for i in range(1,no_seats+1):
            # This is used for the recorrect the seat number
                def recorrect():             
                   book_seats=int(input(f"{i} which seat no you want to book "))
                   if book_seats in vip_seat:    
                      vip_seat.remove(book_seats)
                      print( "   ", vip_seat) 
                   elif book_seats not in vip_seat and 0<book_seats<31:
                      print(f"{i} Seat number {book_seats} is already booked: ")
                      recorrect()
                   elif 30<book_seats>101:
                      print(f"{i} Seat number {book_seats} is Not vip")
                      recorrect()
                   # elif book_seats==None:
                   #     print("Enter proper values ")
                   #     recorrect(self)   
                   else:
                      print(f"{i} Please select the seat number 1 - 100")
                      recorrect()
                   self.empty_seat_list=vip_seat                         
                recorrect()
        else:
            print("We dont have that many seats")        
        print(self.empty_seat_list)
        o.vip()
          
        
        
        
    def regulara(self):
        pass
                
        
o=Ceat()
o.vip()
o.regulara()
        
       