
# * Input can also be read from files. Files can be opened using the built-in function open. Using a with <command> as <name> syntax (called a 'Context Manager') makes using open and getting a handle for the file super easy:

# with open('015_IO/test.txt', 'r') as fileobj:
#     pass

# * This ensures that when code execution leaves the block the file is automatically closed.

# * Files can be opened in different modes. In the above example the file is opened as read-only. To open an existing file for reading only use r. If you want to read that file as bytes use rb. To append data to an existing file use a. Use w to create a file or overwrite any existing files of the same name. You can use r+ to open a file for both reading and writing. The first argument of open() is the filename, the second is the mode. If mode is left blank, it will default to r.

# # let's create an example file:
# with open('015_IO/test.txt', 'w') as fileobj:
#     fileobj.write('Hello Mom')
# with open('015_IO/test.txt', 'r') as fileobj:
#     # this method makes a list where each line
#     # of the file is an element in the list
#     lines = fileobj.readlines()
# print(lines)
# # here we read the whole content into one string:
# with open('015_IO/test.txt', 'r') as fileobj:
#     content = fileobj.read()
#     # get a list of lines, just like int the previous example:
#     lines = content.split('\n')
# print(lines)


# * If the size of the file is tiny, it is safe to read the whole file contents into memory. If the file is very large it is often better to read line-by-line or by chunks, and process the input in the same loop. To do that:

with open('015_IO/test.txt', 'r') as fileobj:
    # this method reads line by line:
    lines = []
    for line in fileobj:
        lines.append(line.strip())
print(lines)

# * Opened files (fileobj in the above examples) always point to a specific location in the file. When they are first opened the file handle points to the very beginning of the file, which is the position 0. The file handle can display its current position with tell:

fileobj = open('015_IO/test.txt', 'r')
pos = fileobj.tell()
print('We are at %u.' % pos)  # We are at 0.
content = fileobj.read()
end = fileobj.tell()
print(content)
print('This file was %u characters long.' % end)
# This file was 22 characters long.
fileobj.seek(7)
pos = fileobj.tell()  # We are at 7.
print('We are at %u.' % pos)
content = fileobj.read(10)  # start at 7 and read 10
end = fileobj.tell()
print(content)
pos = fileobj.tell()  # We are at 18.
print('We are at %u.' % pos)
fileobj.close()

with open('015_IO/test.txt', 'r') as fileobj:
    print(type(fileobj.read()))  # <class 'str'>
with open('015_IO/test.txt', 'rb') as fileobj:
    print(type(fileobj.read()))  # <class 'bytes'>
