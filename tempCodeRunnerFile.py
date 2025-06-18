class Ceat:
    def __init__(self):
        self.vip_empty_ceat_list=[]
        self.general_empty_ceat_list=[]
        self.booked_ceat=[]
    def vip(self):
# print(self.vip_empty_ceat_list)
        vip_seat=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,7,28,29,30]
        print(vip_seat)
        no_seats=int(input("Enter the number of seats to book: "))            
        if 0<no_seats<30:
            for i in range(1,no_seats+1):
            # This is used for the recorrect the seat number
                def recorrect():             
                   self.book_seats=int(input(f"{i} which seat no you want to book "))
                   if self.book_seats in vip_seat:    
                      vip_seat.remove(self.book_seats)
                      print( "   ", vip_seat) 
                   elif self.book_seats not in vip_seat and 0<self.book_seats<31:
                      print(f"{i} Seat number {self.book_seats} is already booked: ")
                      recorrect()
                   # elif book_seats==None:
                   #     print("Enter proper values ")
                   #     recorrect(self)   
                   else:
                      print(f"{i} Please select the seat number 1 - 30")
                      recorrect()
                   self.vip_empty_ceat_list=vip_seat                         
                recorrect()
                
                self.booked_ceat.append(self.book_seats)
                print(self.booked_ceat)
              
        else:
            print("We dont have that many seats")        
        print("still remaining ceat's in VIP: ",self.vip_empty_ceat_list)
        print(self.booked_ceat)
        
o=Ceat()
o.vip()   