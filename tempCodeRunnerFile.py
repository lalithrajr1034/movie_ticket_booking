from functions import movies

#shows

print("""
      1.morning show 
      2.afternoon show
      3.Night show""")
movie_shows=int(input("Enter the shows number : "))
if movie_shows==1:
    print("You have selected Morning show")
    movies.morning_show_movies()
elif movie_shows==2:
    print("You have selected After noon show")
    movies.afternoon_show_movies()
elif movie_shows==3:
    print("You have selected Night show")
    movies.night_show_movies()   
else:
    print("You entered wrong show number")
    


#movie's




#seat type