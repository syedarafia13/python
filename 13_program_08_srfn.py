# Author: Syeda Rafia Fizza Naveed
'''
        Create an empty dictionary. Allow 4 friends to enter their favourite language as values 
and use keys as their names. Assume that the languages of two friends are same; what will to the program?
'''

favLang = {}

a = input("Enter your favorite language Sidra\n")
b = input("Enter your favorite language Nabeehah\n")
c = input("Enter your favorite language Shiza\n")
d = input("Enter your favorite language Fatima\n")

favLang['Sidra'] = a
favLang['Nabeehah'] = b
favLang['Shiza'] = c
favLang['Fatima'] = d

print(favLang)
