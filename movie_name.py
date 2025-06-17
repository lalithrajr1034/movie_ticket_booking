class Movies:  
    def __init__(self):
        pass
  # morning_show
    def morning_show(self):
        self.morning_movie_list={
           
           1:"Pushpaka vimana",
           2:"Bahubali",
           3:"Bhramastra"
       }     
        # it helps to print the movie name 
        for i in self.morning_movie_list:
            print(f"      {i}.{self.morning_movie_list[i]}")
        
        inp_var1=int(input("Enter the movie number "))
        if inp_var1 in self.morning_movie_list:
           print(f"You have seleced :{self.morning_movie_list[inp_var1]}")
        else:
            print("Invalid movie number")   
            
   # Evening show
    def afternoon_show(self):
        self.afternoon_movie_list={
           1:"Family star",
           2:"Babru vahana",
           3:"Karva"
        }
        for i in self.afternoon_movie_list:
          print(f"      {i}.{self.afternoon_movie_list[i]}")
        inp_var2=int(input("Enter the values of the movie"))
        if inp_var2 in self.afternoon_movie_list:
            print(f"you have selected {self.afternoon_movie_list[inp_var2]}")
        else :
            print("invalid movie number")
              
   #Night show
    def night_show(self):
        self.night_movie_list={
            1:"6-3=2",
            2:"365 days",
            3:"night mare"
        }
        for i in self.night_movie_list:
            print(f"      {i}.{self.night_movie_list[i]}")
        inp_var3=int(input("Enter the option"))   
        if inp_var3 in self.night_movie_list:
            print(f"you have selected {self.night_movie_list[inp_var3]}")
        else:
            print("Invalid movie number")    
        
        
 
 
 

#this should be a second value    
        
  
  
  
  
# LEARNING  :

# Instance variable and local-----------
'''
local variable is used only inside that method (It cannot be accessed outside this method) (or) It is created inside the function/methods, used, and then destroyed when the function finishes


Instance variable can acess out of the method by passing the parameter, It is stored in the object created from the class (e.g., obj = movies())
'''
  