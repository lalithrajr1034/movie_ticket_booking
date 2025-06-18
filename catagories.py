class Ceat:
    def __init__(self):
        self.vip_empty_ceat_list=[]
        self.general_empty_ceat_list=[]
        self.vip_booked_ceat=[]
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
                
                self.vip_booked_ceat.append(self.book_seats)
                
              
        else:
            print("We dont have that many seats")        
        print("still remaining ceat's in VIP: ",self.vip_empty_ceat_list)
        print(self.vip_booked_ceat)
        re_book=int(input("Enter the option:\n1.book more\n2.get ticket\n3.Exit "))
        if re_book==2:
           A=len(self.vip_booked_ceat)
           
           print("you have booked ",A," ceats")
           print("1 VIP = 250\n",A,"VIP = ",A*250)
           print("Thankyou.....")
        elif re_book==1:
            print("You can book more here")
            self.vip()   
        else:
            return    
            
    
        
        
        
    def general(self):
        
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
        
        
               