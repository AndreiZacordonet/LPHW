from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv
my_var = input("This is a random var, do what you want with that: ")
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is", third)
print("Random var value: {}".format(my_var))
