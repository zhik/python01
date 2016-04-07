while True:
	#it will try to get the user to enter an float (just to be safe with inputs)
    try:
        hours = float(input("Amount of hours worked: "))
        rate = float(input("Rate for each hour: "))
    #if the user fails , it will trigger except
    except:
        print("You didn't enter a number")
    #it will print an error message and loop
        continue
    else:
    #if no error then it will break while and run the rest
        break
salary = hours * rate
print "Your salary is $", salary

