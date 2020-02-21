######################################################
##### [1] Digital Sum
######################################################
from eulerlib.numtheory import *
print( digital_sum(input_number) )

######################################################
##### [2] Digital Root
######################################################
from eulerlib.numtheory import *
print( digital_root(input_number) )

######################################################
###### [3A] Is it a palindome (in default base 10)?
######################################################
def is_it_a_palindrome(input_number):
    paste_it_here = str(input_number)
    if paste_it_here == str(paste_it_here)[::-1]:
        return True
    else:
        return False
        
######################################################
###### [3B] Is it a palindome in some specific base?
######################################################
from eulerlib.etc import *
print( is_palindrome (input_number_base_10 , base) )
        
######################################################
##### [4] Convert to different number base
######################################################
from eulerlib.etc import *
print( decimal_to_base (input_number_base_10 , base) )

######################################################
##### [5] Is it pandigital (it only contains all the digits from 1 til 9)?
######################################################
from eulerlib.etc import *
input_number_here = 10000
starting_digit = 1
stopping_digit = 9
print ( def is_pandigital(num,starting_digit,stopping_digit) )

######################################################
##### [6] Convert the word into sum of numerical value of each letter in the word based on its position in the alphabet.
######################################################
from eulerlib.etc import *
print ( word_numerical_val('randomword') )
