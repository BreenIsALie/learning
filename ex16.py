# exercise 16: reading and writing files

from sys import argv

script, filename = argv

print "We're going to erase %r" % filename
print "\nIf you don't want that, press CTRL-C (^C)"
print "\nIf you want that, press return"

# holds script until user presses enter as confirmation
raw_input("?")

print "Opening file..."
# opens the file specified when starting the script 
# and save to target variable. uses variable filename
# for selecting the file, and uses "w" string to specify
# write mode. "a" is append, "r" is read. adding a + makes
# it both read and write. default is read-only mode
target = open(filename, "w")

print "Truncating the file. Goodbye"
# empties the file in the target variable before use
target.truncate()

print "Now input three lines"
line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

print "Writing to file"
# writes content of line1 to file target and starts newline
target.write(line1)
target.write("\n")

target.write(line2)
target.write("\n")

target.write("line3")
target.write("\n")

print "Closing file"
target.close()