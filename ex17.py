# exercise 17: more files

from sys import argv
# function for checking if files exist
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# open the file and store it in in_file
in_file = open(from_file)
# take the data from in_file and read it to indata variable
indata = in_file.read()

# use len([filename]) to check file length and print result
print "The input file is %d bytes long" % len(indata)

# checks if file already exists using exist(file)
print "Does the output exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue. CTRL-C to abort"

# hold for user confirmation
raw_input()

# open the output file in write mode
out_file = open(to_file, "w")

# write the contents of indata to outfile
out_file.write(indata)

print "DONE"

# close and save both files
out_file.close()
in_file.close()