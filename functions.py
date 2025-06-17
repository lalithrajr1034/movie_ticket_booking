
def movies():
    movieList={
        1:"Pushpaka vimana",
        2:"Bahubali",
        3:"Bhramastra"
    }
    
    # it helps to print the movie name 
    for i in movieList:
        print(f"{i}.{movieList[i]}")
        
    select_movie=int(input("Enter the movie number "))
    print(f"You have seleced :{movieList[select_movie]}")
        
  