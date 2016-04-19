text = "X-DSPAM-Confidence:    0.8475";
#       0123456789012345678901234567890
#                 1         2   

def find_number(text):   
	decimal = text.find(".")
	if decimal != -1:
		try:
			number = float(text[decimal:])
		except:
			print "there is no float number found"
		print "your number is", number
	else: 
		print "there is no float number found"
		
find_number(text)






