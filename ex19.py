# exercise 19: functions and variables

# defines function, adds arguments to specified variables
def cheese_and_crackers (cheese_count, box_of_crackers):
	print "you have %d cheeses" % cheese_count
	print "you hve %d boes of crackers" % box_of_crackers

print "we can just give the function numbers directly"
# gives the values directly instead of putting
# them in a variable first
cheese_and_crackers (20, 30)

print "OR we can use variables from our script"
# adds the values into variables for use in the script
# instead of directly giving them to the function
amount_of_cheese = 10
amount_of_crackers = 50

# runs function with the previously given variables
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "we can even do math inside too:"
# adds the values, but does math to produce the end result
# directly in the variable call
cheese_and_crackers(10 + 20, 5 + 6)

print "and we can conbine the two, variables and math"
# combination of all to show off mostly
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

