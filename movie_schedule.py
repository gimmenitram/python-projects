# current_movies = {}
# current_movies ['The Grinch'] = '11:00am'

current_movies = {'The Grinch':'11:00am',
                    'Rudolph':'1:00pm',
                    'Frosty the Snowman':'3:00pm',
                    'Christmas Vacation':'5:00pm'}
movies_lower = {k.lower():v for k,v in current_movies.items()}                    

print("We're showing the following movies:")
for key in current_movies:
    print(key)
movie = input('What movie would you like the showtime for?\n')
#showtime = current_movies.get(movie)
showTimeLower = movies_lower.get(movie.lower())

if showTimeLower == None:
    print("Requested movie is not playing.")
else:
    print(movie, 'is showing at', showTimeLower)