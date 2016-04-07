"""
Write a program to prompt the user for hours and rate per hour using raw_input to compute gross pay. 
Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. 
Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
You should use raw_input to read a string and float() to convert the string to a number. 
"""
while True:
    try:
        hours = float(input("Amount of hours worked: "))
        rate = float(input("Rate for each hour: "))
    except:
        print("You didn't enter a number")
        quit = raw_input("Do you want to quit (y)? ")
        if quit == "y":
           break
        continue
    else:
        if hours > 40:
           salary = hours * rate + ((hours - 40) * (rate * .5))
        elif hours <= 40:    
           salary = hours * rate
        print "Your salary is $", salary
        break
print "Goodbye"


