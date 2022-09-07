# Author Joshua Bare
# Application teaching users how to use and apply python enum functions, lists, and for loops
# Hard printing comments to guide user in directions of the application


name = input("How rude of me, I didnt get your name. You are? ")

print (name, ", today we'll write a bit of code to print a list using the enum function.")

months = ["January, ", "February, ", "March, ", "April, ", "May, ", "June, ", "July, ", "August, ", "September, ", "October, ", "November, ", "December, "]

greeting = ["Happy New year!", "Will you be my Valentine?", "Mardi Gras!", "I like putting on trim, APRIL FOOLS!", "Happy Mothers day!", "Happy Fathers day!", "Happy Independance Day!", "Happy bday to my second born!", "Remembering September 11", "Trick or Treat!", "Happy turky month!", "Merry Christmas!"]

# Now we’ll show you how to use to a for loop to print the month with a python built in function called enumerate.

print(name,"! Now that you’ve created your calendar list & monthly greetings, we’ll print your list using the enumerate or enum function!")

for c, (value1, value2) in enumerate(zip(months, greeting)): 

# This is telling the code to tell us the number of each listed item in order that it is listed.

# Due to using a zip function, we'll have to tell the program to add 1 to the value of starting integers (0) in order for January to start as the "1" first month of the year.

        print("Month",c+1,", is", value1 + value2)

# This will print the months listed with a integer in order – if the user created their list in proper calendar order, the months will be numbered correctly.

print(name, ", Thanks for playing my game! Don't forget, the real world is the only place to get a decent meal - James Halliday")