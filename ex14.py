# exercise 14: promtpting and passing

# import argv to call arguments from cmd line
from sys import argv

# unpack two variables into script and user_name
script, user_name = argv

# store the raw_input() prompt as it's own variable
prompt = ">> "

# write first prompt, call user_name and script value from cmd line
print "Hi %s, i'm the %s script" % (user_name, script)
print "query %s" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, first response was %r
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)
