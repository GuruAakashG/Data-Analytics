import imdb
 
# creating instance of IMDb
ia = imdb.IMDb()
 
# movie name
name = "3 idiots"
 
# searching the movie
search = ia.search_movie(name)
 
# printing the result
for i in search:
    print(i)