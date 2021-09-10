# Author: Syeda Rafia Fizza Naveed
'''
        Create an empty dictionary. Allow 4 friends to enter their favourite language as values 
and use keys as their names. Assume that the names of two friends are same; what will to the program?
'''

favLang = {}

a = input("Enter your favorite language Sidra\n")
b = input("Enter your favorite language Nabeehah\n")
c = input("Enter your favorite language Nabeehah\n")
d = input("Enter your favorite language Fatima\n")

favLang['Sidra'] = a
favLang['Nabeehah'] = b
favLang['Nabeehah'] = c
favLang['Fatima'] = d

print(favLang)