# exercise 6: strings and text

# string with variable outside of string stored as x variable
x = "there are %d types of people" % 10
# simple strings saved as variables
binary = "bindary"
do_not = "don't"
# string with two external variables stored as y variable
y = "those who know %s and those who %s" % (binary, do_not)

# print the strings and add in the values stored outside at the %s and %d locations
print x
print y

# print whole string stored in x inside the string as raw format
print "i said: %r." % x
print "i also said: '%s'." % y

# boolean value stored in variable
hillarious = False
# store string with options for raw input in variable
# no variable given here as it is given when the string is read
joke_evaluation = "isn't that joke so funny! %r"

# print the string stored and give it the variable hillarious
# variable is given to the strng here
print joke_evaluation % hillarious

w = "this is the left side of..."
e = "a string with a right side"

# prints variable e right after w, making a complet sentance
print w + e





