import itertools
import os
with open('016_Files_Folders_IO/test.txt', 'r') as fp:
    for line in fp:
        print(line, end="")

with open('016_Files_Folders_IO/test.txt', 'r') as fp:
    while True:
        cur_line = fp.readline()
        # If the result is an empty string
        if cur_line == '':
            # We have reached the end of the file
            break
        print(cur_line, end="")
    print()

with open("016_Files_Folders_IO/test.txt", "r") as fp:
    lines = fp.readlines()
    print(lines)
for i in range(len(lines)):
    print("Line " + str(i) + ": " + lines[i], end="")

# for root, folders, files in os.walk('./'):
#     for filename in files:
#         print(root, filename)

# ~ Getting the full contents of a file

# * The preferred method of file i/o is to use the with keyword. This will ensure the file handle is closed once the reading or writing has been completed.

with open('016_Files_Folders_IO/test.txt') as in_file:
    content = in_file.read()
print(content)

# * Manual Close

in_file = open('016_Files_Folders_IO/test.txt', 'r')
content = in_file.read()
print(content)
in_file.close()

# ! Keep in mind that without using a with statement, you might accidentally keep the file open in case an unexpected exception arises like so:

# in_file = open('016_Files_Folders_IO/test.txt', 'r')
# # raise Exception("oops")
# in_file.close()  # ! This will never be called

# * So let's suppose you want to iterate only between some specific lines of a file
# * You can make use of itertools for that

print()
with open('016_Files_Folders_IO/test.txt', 'r') as f:
    for line in itertools.islice(f, 12, 14):
        print(line, end="")
        # do something here
