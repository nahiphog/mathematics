######################################################
###### [1] Find the Greatest Common Divisor (GCD) of 2 numbers.
######################################################
from eulerlib.numtheory import *
first_number, second_number = 7, 14 # INPUT VALUES HERE
print( gcd(first_number , second_number) )

######################################################
###### [2] Find the Lowest Common Divisor (LCM) of a list of numbers.
######################################################
from eulerlib.numtheory import *
list_of_integers = [ 3 , 5 , 7, 11 ] # INPUT VALUES HERE
print ( lcm_n( list_of_integers ) )

