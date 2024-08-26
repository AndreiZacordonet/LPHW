# imports argv dynamic object for sys module
from sys import argv

# unpackaging the arguments
script, filename = argv

# opening the file in read text mode
txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())   # reading the content of the file

# print("Type the filename again:")
# file_again = input("> ")
#
# # opening file in read text mode
# txt_again = open(file_again)
#
# # reading the content of the file
# print(txt_again.read())

file_again = input("Ihre Dateinamen bitte: ")   # Datei means file
print("Ihre Dateiinhalt ist: {}".format(open(file_again).read()))
