with open('016_Files_Folders_IO/test.txt', 'w') as f:
    f.write("Hello Mom!\n")
    f.write("Hello Mom!\n")
    f.write("Hello Mom!\n")
    f.write("Hello Mom!\n")

# * Python doesn't automatically add line breaks, you need to do that manually

# If you want to specify an encoding, you simply add the encoding parameter to the open function:
with open('016_Files_Folders_IO/test.txt', 'w', encoding='utf-8') as f:
    f.write('Hello Mom with utf-8 text')


# * It is also possible to use the print statement to write to a file. The mechanics are different in Python 2 vs Python 3, but the concept is the same in that you can take the output that would have gone to the screen and send it to a file instead.

with open('016_Files_Folders_IO/test.txt', 'w') as outfile:
    s = "Hello Mom!!"
    print(s)  # writes to stdout
    print(s, file=outfile)  # writes to outfile
    # Note: it is possible to specify the file parameter AND write to the screen by making sure file ends up with a None value either directly or via a variable
    myfile = None
    print(s, file=myfile)  # writes to stdout
    print(s, file=None)  # writes to stdout
