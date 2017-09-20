# exercise 8: printing, printing

# stores a string with places where values will be added
# by using %r it can adapt to any input
# NOTE: using %r is best left for debugging, not prod
formatter = "%r %r %r %r"

# prints formatter and gives it four numeric values
print formatter % (1, 2, 3, 4)

# same as above, but with string values instead
print formatter % ("one", "two", "three", "four")

# here with boolean values
print formatter % (True, False, False, True)

# since %r gives the raw data of a variable, the formatter variable here will show 
# the value that it was originally given, not with any other data added
# so the output is the code itself
print formatter % (formatter, formatter, formatter, formatter)

# string is broken into it's own lines in the code, but joins together
# using the comma after each string. functionally the same as line 12,
# just coded differently

print formatter % (
	"i had this thing",
	"that you could type up right",
	"but it didn't sing",
	"so i said goodnight",
	)
