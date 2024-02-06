txt = "The quick brown fox jumps over the lazy dog."
t1 = "fox"
t2 = "cat"

###############################################################################
# DONE: 1. (6 pts)
#
#   Write each of the functions below (each that takes two parameters and uses
#   the appropriate operator from the reading) that simply returns the boolean
#   evaluation of those two parameters:
#
#   equal()
#   not_equal()
#   greater_than()
#   less_than()
#   greater_than_or_equal_to()
#   less_than_or_equal_to()
#
#   Now write a line of code for each one using numbers for the parameters that
#   would cause each function to return True. 
#   
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
def equal(x, y):
    print(bool(x == y))
def not_equal(a, b):
    print(bool(a != b))
def greater_than(c, d):
    print(bool(c > d))
def less_than(e, f):
    print(bool(e < f))
def greater_than_or_equal_to(g, h):
    print (bool(g >= h))
def less_than_or_equal_to(i, j):
    print(bool(i <= j))
equal (3, 3)
not_equal(3, 4)
greater_than(4, 3)
less_than(3, 4)
greater_than_or_equal_to(4, 3)
less_than_or_equal_to(3, 4)

###############################################################################
# DONE: 1. (2 pts)
#
#   Write a line of code that returns True if the string
#       t1 (defined above)
#   is contained in the string
#       txt (also defined above)
#   and prints the result.
#
#   Write another line of code that returns True if the string
#       t2
#   is contained in the string
#       txt
#   and prints the result.
#
#   Run your code. Does it return what you expect?
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

print(t1 in txt)
print(t2 in txt)

###############################################################################
# DONE: 1. (1 pt)
#
#   Now, write a line of code that returns True if the string
#       t1
#   is *not* the same thing as
#       t2
#   and prints the result
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

print(t1 is not t2)