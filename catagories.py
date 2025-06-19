class Ceat:
    def __init__(self):
        self.vip_empty_ceat_list=[]
        self.vip_booked_ceat=[]
        self.general_empty_ceat_list=[]
        self.general_booked_ceat=[]
        
    def book_more_seats(self,listt):
        self.list=listt
        end=len(self.list)
        print(self.list)
        no_seats=int(input("Enter the number of seats to book: "))  
        if 0 < no_seats <=end:
            for i in range(1,no_seats):
                def recorrecct():
                    self.re_book_seats=int(input(f"{i} Enter which seats to book : "))
                    if self.re_book_seats in self.listt:    
                       self.list.remove(self.re_book_seats)
                       print( "   ", self.list) 
                    elif self.re_book_seats not in self.list and 0<self.re_book_seats<end:
                       print(f"{i} Seat number {self.re_book_seats} is already booked: ")
                       recorrecct()
                   # elif book_seats==None:
                   #     print("Enter proper values ")
                   #     recorrect(self)   
                    else:
                      print(f"{i} Please select the seat number 1 - {end}")
                      recorrecct()           
        else:
            print("More number of seats are not available")
        
        
        
        
        
        
         
    def vip(self):
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
        print("still remaining seat's in VIP: ",self.vip_empty_ceat_list)
        print("Booked seat's",self.vip_booked_ceat)
        re_book=int(input("\n1.book more\n2.get ticket\n3.Exit \nEnter the option:"))
        if re_book==2:
           A=len(self.vip_booked_ceat)          
           print("\nyou have booked ",A," seats")
           print(" 1 VIP = 250\n",A,"VIP = ",A*250)
           print("Thankyou.....\n\n")
        elif re_book==1:
            print("You can book more seat")
            self.st=0
            self.end=31
            self.book_more_seats(self.vip_empty_ceat_list)  #--------------------------------------------------------------------------
            
        else:
            return    
       
    def general(self):       
        general_seat=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70]
        print(general_seat)
        num_ceat=int(input("Enter the nuber of seat: "))
        if 0<num_ceat<70:
            for i in range(1,num_ceat+1):
                def repeated():
                    ceat_no=int(input(f"{i}.Enter the seat number :"))
                    if ceat_no in general_seat:
                        general_seat.remove(ceat_no)
                        print(general_seat)
                    elif ceat_no>70:
                        print("  we have only max 70 seat")    
                        repeated()
                    else:
                        print(f"  ceat number {ceat_no} already booked")    
                        repeated()
                    self.general_booked_ceat.append(ceat_no)    
                repeated()
             
        else:
            print("we dont have many seats")
        self.general_empty_ceat_list=general_seat    
        print("\n\n\nstill remaining seats",self.general_empty_ceat_list)   
        print("\nBooked ceat,s",self.general_booked_ceat)
        re_book=int(input("\n1.book more\n2.get ticket\n3.Exit \nEnter the option:"))
        if re_book==2:
           A=len(self.general_booked_ceat)
        #    print(Mov.ticket_variable[0])
           print("\n you have booked ",A," seats")
           print(" 1 VIP = 250\n",A,"VIP = ",A*250)
           print("Thankyou.....\n\n")
        elif re_book==1:
            print("You can book more seat")
            self.book_more_seats(self.general_empty_ceat_list)   
        else:
            return  
        
        
        
            
c=Ceat()
# c.vip()
c.general()               