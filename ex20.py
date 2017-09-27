# exercise 20: functions and files

from sys import argv

script, input_file = argv 

# function to read the file specified when running the variable.
# saves the file in f variable and then uses read()
def print_all(f):
	print f.read()

# moves the "read head" back to positin byte 0 (start of file) using seek
# seek moves a read head to a designated position in the file
def rewind(f):
	f.seek(0)

# takes amount of lines and a file, then reads the specified amount
# of lines from the file. this is how tail [nr] works on linux
def print_a_line(line_count, f):
	print line_count, f.readline()

# opens the file specified and saves it to the current_file variable
current_file = open(input_file)

print "first, lets print the whole file:\n"
# runs print_all and gives it the value of current_file to use. 
# print_all becomes f in the function
print_all(current_file)

print "now lets rewind, like a tape"
# same as above, but now current_file gets used with rewind function
# moves to position byte 0 in the file
rewind(current_file)

print "lets print three lines:"
# uses the variable set to 1 and the file in current_file to print
# only one line from the file in current_file
current_line = 1
print_a_line(current_line, current_file)

# same as above, but now the variable current_line (with value already set to 1)
# gets added to by 1, making the value 2. so function prints two lines
current_line = current_line + 1
print_a_line(current_line, current_file)

# same as above, but with another 1. so value in current_line is now 3
# therefore it prints 3 lines
current_line = current_line + 1
print_a_line(current_line, current_file)