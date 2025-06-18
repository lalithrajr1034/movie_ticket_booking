from movie_name import Movies

obj=Movies()

#  Seats and Categories
"""
VIP      30   250
GENERAL  70   150 
"""


class Ceat:
    def __init__(self):
        self.vip_empty_ceat_list=[]
        self.general_empty_ceat_list=[]
        
    def vip(self):
# print(self.vip_empty_ceat_list)
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
                   # elif book_seats==None:
                   #     print("Enter proper values ")
                   #     recorrect(self)   
                   else:
                      print(f"{i} Please select the seat number 1 - 30")
                      recorrect()
                   self.empty_ceat_list=vip_seat                         
                recorrect()
        else:
            print("We dont have that many seats")        
        print(self.vip_empty_seat_list)
# o.vip()
          
        
        
        
    def general(self):
        self.general_empty_ceat_list
        general_seat=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70]
        print(general_seat)
        num_ceat=int(input("Enter the nuber of seat: "))
        if 0<num_ceat<70:
            for i in range(1,num_ceat+1):
                def repeated():
                    ceat_no=int(input(f"{i}.Enter the ceat number :"))
                    if ceat_no in general_seat:
                        general_seat.remove(ceat_no)
                        print(general_seat)
                    elif ceat_no>70:
                        print("  we have only max 70 ceat")    
                        repeated()
                    else:
                        print(f"  ceat number {ceat_no} already booked")    
                        repeated()
                repeated()
             
        else:
            print("we dont have many seats")
        self.general_empty_ceat_list=general_seat    
        print(self.general_empty_ceat_list)   
        
        
                
        
o=Ceat()
# o.vip()
# o.general()
        
v=o.general_empty_ceat_list
print(v)
