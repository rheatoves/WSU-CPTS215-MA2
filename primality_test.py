##############################################
# Title: MA2 - Primality Test
# Author: Rhea Toves
# Version: 1.0
# Date: January 22, 2022
#
# Description: This program receives (int)
# input from the user, defines the number
# as prime or not prime. The program will then
# calculate the sum of prime numbers.
##############################################
import math

n = int(input("Please enter an integer >= 2: "))

def is_prime(n):
    initial = 2
    square = math.sqrt(n)
    while initial <= square:
        if n % initial == 0:
            return False
        initial += 1;
    return True

while is_prime(n) == True:
    if n < 2:
        print("Looks like you've entered an integer less than 2, please try again.")
        break
    else:
        break

if is_prime(n) == True:
    print(n, "is a prime number!")
else:
    print(n, "is not a prime number!")

def sum_primes(m):
    sum_prime = 0
    for initial2 in range(2, m+1):
        if is_prime(initial2):
            sum_prime += initial2
    return sum_prime

print("Sum of primes from 2 to", n, "is", sum_primes(n))