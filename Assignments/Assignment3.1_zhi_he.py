while True:
    try:
        hours = float(input("Amount of hours worked: "))
        rate = float(input("Rate for each hour: "))
    except:
        print("You didn't enter a number")
        continue
    else:
        break

if hours > 40:
   salary = hours * rate + (rate * .5)
elif hours <= 40:    
   salary = hours * rate

print "Your salary is $", salary

