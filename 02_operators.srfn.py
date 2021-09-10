# Name: SYEDA RAFIA FIZZA NAVEED
# Program of Operators in Python.
a = 1
b = 3

'''  ******* ARTHIMETIC OPERATORS *******  '''

print("The value of 1+3 is,",1+3)
print("The value of 1-3 is,",1-3)
print("The value of 1*3 is,",1*3)
print("The value of 1/3 is,",1/3)

'''  ******* ASSIGNMENT OPERATORS *******  '''

a = 13
a += 2               # =+ shortcut for adding 2 in 13
a -= 2               # =+ shortcut for subtracting 2 in 13
a *= 2               # =+ shortcut for multiplying 2 in 13
a /= 2               # =+ shortcut for divided 2 in 13
print(a)

'''  ******* COMPARISON OPERATORS *******  '''

# b = (5>3)
# b = (5>=3)
# b = (5<3)
# b = (5<=3)
# b = (5==3)
b = (5!=3)         # 5 is not equal to 3
print(b)

'''  ******** LOGICAL OPERATORS *********  '''

bool1 = True
bool2 = False
print("The value of bool1 and bool 2 is", (bool1 and bool2)) # and only return TRUE when both are TRUE otherwise it return FALSE
print("The value of bool1 or bool 2 is", (bool1 or bool2))   # Or return TRUE when any of one is TRUE
print("The value of not bool 2 is", (not bool2))             # not print opposite : if it is FALSE not operator ptint TRUE