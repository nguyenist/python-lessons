# Goal #1: Create a program that will print out a list of movie titles and a set of ratings defined below into a particular format.



# First, choose any five movies you want.

# Next, look each movie up manually to find out four pieces of information:
#		Their parental guidance rating (G, PG, PG-13, R)
#		Their Bechdel Test Rating (See http://shannonvturner.com/bechdel or http://bechdeltest.com/)
#		Their IMDB Rating from 0 - 10 (See http://imdb.com/)
# 		Their genre according to IMDB

# After a few more lessons, you'll be able to tell Python to go out and get that information for you, but for now you'll have to collect it on your own.

# Now that you've written down each piece of information for all five of your movies, save them into variables.

# You'll need a variable for movie_titles, a variable for parental_rating, a variable for bechdel_rating, a variable for imdb_rating, and a variable for genre.

movie_titles = ['101 Dalmations','13 Going on 30','American Zombie','Food Stamped','The Bourne Identity']
parental_rating = ['G','PG-13','Unrated','R','G']
bechdel_rating = ['3/3', '3/3', '3/3', '3/3', '1/3']
imdb_rating = ['7.2','6.1','5.1', '6.5', '7.9']
genre = ['Animation','Comedy','Horror','Documentary','Thriller']

# Since you have five sets of facts about five movies, you'll want to use lists to hold these pieces of information.

# Once all of your information is stored in lists, loop through those lists to print out information with each part separated by a comma, like this:

# Example:
# Jurassic Park, PG-13, 3, 8.0, Adventure / Sci-Fi
# Back to the Future, PG, 1, 8.5, Adventure / Comedy / Sci-Fi

dataArray = zip(movie_titles, parental_rating, bechdel_rating, imdb_rating, genre)
for movie_titles, parental_rating, bechdel_rating, imdb_rating, genre in dataArray:
    print "{0}, {1}, {2}, {3}, {4}".format(movie_titles, parental_rating, bechdel_rating, imdb_rating, genre)

# Note how each piece of information is separated by a comma.  This is a specific file format called the "Comma Separated Value (CSV)" format
# If you can make a CSV file, you can open it up in Excel or Numbers as a spreadsheet.

# When you've printed out your information like the example above, copy/paste that into a file and save it as a .csv file.
# Open that up in Excel, Numbers, or another spreadsheet program.  How does it look?
# To see an example of how it should look, check out: https://github.com/shannonturner/python-lessons/blob/master/section_05_(loops)/movies.csv









