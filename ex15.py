# exercise 15: reading files

from sys import argv

script, filename = argv

# open file specified from cmd line, giving the script access to it
txt = open(filename)

print "Here is your file %r" % filename
# reads the file that was opened on line 8, and prints it
print txt.read()
# closes file after reading it, saving the file
txt.close()

print "Type the filename again"
# get file name from user for second file
file_again = raw_input('> ')

# open the file so the script can read it
txt_again = open(file_again)

# read from the opened file and print it
print txt_again.read()
# closes txt_again after use, saving the file
txt_again.close()




