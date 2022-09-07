# Author Joshua Bare


#Weekly Pay
name = input("Please enter your name:") # Asking user input for name

# Name prompt requested

print ("Hello, " 'name') 			

# Acknowledging user name input

hoursworked = input("Please enter your hours worked this week: " )  # Asking user for hours worked

# Prompt for user input

hourlyrate = input("Please enter your hourly rate: ")			# Asking user for hourly rate

# Prompt for user input

print ("Hello, "+ name + , ".", "You worked ", hoursworked, "at a rate of ", hourlyrate, ".", "Is that correct?") 				# Printer users greeting with input
correct = input("y for yes or n for no.")
if correct == "y":
    print("Excellent!")
else:
    print ("Please refresh the page and begin again!")
    
complete = input("Are you finished? y for yes or n for no.")

if finished == "y":
    print("Okay, bye!")
else:
    print ("Please refresh the page and begin again!")
complete = ["We're all done!"] 			# End of program prompt loop
for x in complete:
    print (x)
