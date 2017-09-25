# exercise 18: names, variables, code, functions

# define function, tell it to expect arguments and add as list
def print_two(*args):
	# unpack arguments from function call to functions arg1 and arg2
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# define function, do the unpacking in the function call itself
# the two arguments called will be put in arg1 and arg2
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# same as above, but with one argument
def print_one(arg1):
	print "arg1: %r" % arg1

# same as above, with no arguments
def print_none():
	print "I got nothing"

# runs funtions created above, and gives them the arguments
# as strings when calling the function (apart from last)
print_two("zed", "shaw")
print_two_again("zed", "shaw")
print_one("first")
print_none()