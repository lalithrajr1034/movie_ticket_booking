from movie_name import Movies
from catagories import *



# object------
m_name=Movies()
catagory=Ceat()


# shows and movies 
class MainFunction:
    def __init__(self):
        self.t=3
    def shows(self):
        print("""
          1.morning show 
          2.afternoon show
          3.Night show""")
        movie_shows=int(input("Enter the shows number : "))
        if movie_shows==1:
            print("You have selected Morning show\n")
            m_name.morning_show()
        elif movie_shows==2:
            print("You have selected After noon show\n")
            m_name.afternoon_show()
        elif movie_shows==3:
            print("You have selected Night show\n")
            m_name.night_show()   
        else:
            print("You entered wrong show number\n\n")
  
    
ob=MainFunction()
ob.shows()

print(catagory.vip_empty_ceat_list,"hi lalith")
