while True:
    try:
        score = float(input("Enter a score between 0.0 and 1.0: "))
    except:
        print("You didn't enter a number")
        continue
    else:
        break

if score > 1.0:
	print "this isn't between 0.0 and 1.0"
elif score >= .9:
   print "A"
elif score >= .8:
   print "B"
elif score >= .7:
   print "C"
elif score >= .6:
   print "D"
elif score < .6:
   print "F"

