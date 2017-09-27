# exercise 21: functions can return something

# function for addition, takes two values into variable a and b
def add(a, b):
	# prints the value that it was given in the string.
	# no math is done here
	print "ADDING %d + %d" % (a, b)
	# math is done directly in the return function. return takes
	# something done in the function and returns it to
	# the outside of the funtion.
	return a + b

def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b

print "Lets do some math with just functions"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "AGE: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# function-in-function example. Read the row backwards and
# you get the order of the math functions
print "Here is a puzzle\n"
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "\n\nThat becomes: ", what, "Can you add it by hand?"
