# Write a program that prompts for a file name, then opens that file and reads 
#through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475

# Count these lines and extract the floating point values from each of the lines and compute 
# the average of those values and produce an output as shown below. 
# Do not use the sum() function or a variable named sum in your solution.

# if " " in line:
fname = raw_input("Enter file name: ")
n_list = []

try:
	fh = open(fname)
except:
	print "this isn't a file"

for line in fh:
	line = line.lstrip().rstrip()
	if line.startswith("X-DSPAM-Confidence:"):
		decimal = line.find(".")
		number = float(line[decimal:])
		n_list.append(number)

n_sum = 0
count = 0
for number in n_list:
	n_sum = n_sum + number
	count += 1
average = n_sum / count
print "this is the average", average


