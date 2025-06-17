
def movies():
    movieList={
        1:"Pushpaka vimana",
        2:"Bahubali",
        3:"Bhramastra"
    }
    key = 1
    if key in movieList:
        print(key)
        print(f"{key}.{movieList[2]}")
movies()   