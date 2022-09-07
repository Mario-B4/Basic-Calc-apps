# Author Joshua Bare
# This is a basic calculator application - allowing users to calculate weekly salary and a vehicles MPG

print("Hello, we're going to calculate your weekly salary and MPG.")
print("Please follow the prompts accordingly.")

answer = "yes"
while answer == "yes":

    name = input("Hello, what is your name? ")

    hourlyrate = int(input("Hey " + name + ", what is your hourly pay rate? "))
    hoursworked = int(input("Okay and how many hours did you work this week? ")) 

    pay = hourlyrate * hoursworked

    print(name, ", your pay for this period is $", hourlyrate, " per hour x", hoursworked, "hours worked = $", pay)

    answer = input("Would you like to calculate another wage, yes or no?")
    if answer == "no":
        print("Alright, MOVING ON!")
        
print("Now we're going to calculate your MPG!")
print("Please follow the prompts accordingly.")

answer = "yes"
while answer == "yes":
    
    milesdriven = int(input("How many miles did you drive? "))
    gasused = int(input("Alright, and how many gallons of gas did you use? "))
    
    mpg = milesdriven / gasused
    
    print(name, ", based on the ", milesdriven, "miles you drove, and the ", gasused, "gallons of gas you used. Your MPG is ", mpg)
    
    answer = input("Would you like to calculate another MPG, yes or no?")
    if answer == "no":
        print("Alright, goodbye!")
