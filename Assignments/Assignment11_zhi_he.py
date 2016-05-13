import re
#find all numbers and put them in a list
numbers = re.findall('[0-9]+', open('regex_sum_242232.txt').read())

#find the sum, by going threw all the strings of the list and coverting to intergers
n_sum = 0
for i in range(0,len(numbers)):
	n_sum = n_sum + int(numbers[i])
print n_sum

#other ways

#using list comprehensions 
print sum([int(i) for i in re.findall('[0-9]+',open('regex_sum_242232.txt').read())])

#using map 
print sum(map(int, re.findall('[0-9]+',open('regex_sum_242232.txt').read())))