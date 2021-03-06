######################################################
###### [1A] Generate and keep a list of Fibonacci numbers using recursion
######################################################
list_of_fibonacci_numbers = [0,1]

def generate_fibonacci_numbers():
    list_of_fibonacci_numbers.append( list_of_fibonacci_numbers[-1] + list_of_fibonacci_numbers[-2] )
    
how_many_positive_fibonacci_you_want = 50 # Edit here
for element in range(how_many_positive_fibonacci_you_want - 1):
    generate_fibonacci_numbers()

######################################################
###### [1B] Generate and keep a list of Fibonacci numbers using recursion but don't keep any previous smaller terms
######################################################
list_of_fibonacci_numbers = [0,1]

def generate_fibonacci_numbers_and_keep_last_two():
    list_of_fibonacci_numbers.append( list_of_fibonacci_numbers[-1] + list_of_fibonacci_numbers[-2] )
    list_of_fibonacci_numbers.pop(0)

up_to_which_fibonacci_number = 100 # Edit here
for element in range(1, up_to_which_fibonacci_number):
    generate_fibonacci_numbers_and_keep_last_two()
     
######################################################
###### [2A] Summon via library: Generate how many Fibonacci numbers
######################################################
from eulerlib.fibonacci import *
how_many_fibonacci_numbers = 123
print( first_n_fibo(how_many_fibonacci_numbers, start = 1) )

######################################################
######## [2B] Summon via library: Get the all the Fibonacci number less than N
######################################################
from eulerlib.fibonacci import *
largest_fibonacci_number_less_than = 123
print( fibo_less_than(largest_fibonacci_number_less_than, start = 1) )
