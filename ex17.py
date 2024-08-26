from sys import argv
from os.path import exists

# script, from_file, to_file = argv
#
# print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how

# print(f"THe input file is {len(indata)} bytes long")

# print(f"Does the output file exists? {exists(to_file)}")
# print("Ready, hit RETURN to continue, CTRL-C to abort.")
# input()

open(argv[2], 'w').write(open(argv[1]).read())

# print("Alright, all done.")
#
# out_file.close()
# in_file.close()
