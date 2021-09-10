# Write a program to greet all the persons names stored in a list l1 and which start with s.
#                      l1 = ["Rafia", "Sidra", "Shiza", "Nabeehah"]              

l1 = ["Rafia", "Sidra", "Shiza", "Nabeehah"]

for name in l1:
    if name.startswith("S"):
        print("Hello " + name)