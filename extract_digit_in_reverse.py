#Exercise 11: Write a Program to extract each digit from an integer in the reverse order.
#For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.

#Integer to string and reverse it
def reverse_digits(number):
    reversed_string = str(number)[::-1]

#Print each digit with space separating them
    result = ' '.join(reversed_string)
    print(result)
