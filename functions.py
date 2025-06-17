class movies:  
    def __init__(self):
        pass
  # morning_show
    def morning_show_movies(self):
        movieList={
           
           1:"Pushpaka vimana",
           2:"Bahubali",
           3:"Bhramastra"
       }     
        # it helps to print the movie name 
        for i in movieList:
            print(f"      {i}.{movieList[i]}")
        
        select_movie=int(input("Enter the movie number "))
        if select_movie in movieList:
           print(f"You have seleced :{movieList[select_movie]}\n\n")
        else:
            print("Invalid movie number")   
            
   # Evening show
    def afternoon_show_movies(self):
        pass
      
              
   #Night show
    def night_show_movies(self):
        pass
 
 
 

#this should be a second value    
        
  