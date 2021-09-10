# Author: SYEDA RAFIA FIZZA NAVEED

# Program to fillin a letter template given below with name and date.
#                letter = '''Dear<|NAME|>,
#                            You are selected!
#                            Thanks & Regards,
#                            <|DATE|>'''


letter = '''Dear<|NAME|>,
You are selected!
Thanks & Regards,
<|DATE|>'''

name = input("Enter your Name\n")
date = input("Enter Date\n")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print(letter)

