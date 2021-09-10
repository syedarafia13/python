# Author: SYEDA RAFIA FIZZA NAVEED
# Program of String Slicing

# greeting = "Good Morning, "
# name = "RAFIA FIZZA"
# print(type(greeting))
# print(type(name))

'''************** Concatenating two strings ***************'''
# c = greeting + name
# print(c)

'''************** String Slicing ***************'''
name = "RAFIA FIZZA"
#print(name[0])
# name[2] = "b" --> Does not work

# print(name[1:4])                          # 1 is including , 4 is excluding e.g 123 means print AFI
# print(name[:11])                           # is same as name[0:11]
# print(name[1:])                           # is same as name[1:11]
# c = name[-11:-1]                           # is same is name[1:11]
# print(c)

name = "RafiaFizzaIsGood"    
# d = name[0::3]        # Print R skip af ,print i skip aF ,print i skip zz ,print a skip Is ,print G skip oo ,print d
d = name[:0:-1]         # Print string in reverse order
print(d)