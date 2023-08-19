
# * When it comes to storing, reading, or communicating data, working with the files of an operating system is both necessary and easy with Python. Unlike other languages where file input and output requires complex reading and writing objects, Python simplifies the process only needing commands to open, read/write and close the file. This topic explains how Python can interface with files on the operating system.

# ~ File modes

# ^ There are different modes you can open a file with, specified by the mode parameter. These include:

# * 'r' - reading mode. The default. It allows you only to read the file, not to modify it. When using this mode the
# * file must exist.

# * 'w' - writing mode. It will create a new file if it does not exist, otherwise will erase the file and allow you to write to it.
# * 'a' - append mode. It will write data to the end of the file. It does not erase the file, and the file must exist for this mode.

# * 'rb' - reading mode in binary. This is similar to r except that the reading is forced in binary mode. This is also a default choice.

# * 'r+' - reading mode plus writing mode at the same time. This allows you to read and write into files at the same time without having to use r and w.

# * 'rb+' - reading and writing mode in binary. The same as r+ except the data is in binary

# * 'wb' - writing mode in binary. The same as w except the data is in binary.

# * 'w+' - writing and reading mode. The exact same as r+ but if the file does not exist, a new one is made. Otherwise, the file is overwritten.

# * 'wb+' - writing and reading mode in binary mode. The same as w+ but the data is in binary.

# * 'ab' - appending in binary mode. Similar to a except that the data is in binary.

# * 'a+' - appending and reading mode. Similar to w+ as it will create a new file if the file does not exist. Otherwise, the file pointer is at the end of the file if it exists.

# * 'ab+' - appending and reading mode in binary. The same as a+ except that the data is in binary

# ~ Python 3 added a new mode for exclusive creation so that you will not accidentally truncate or overwrite and existing file.

# * 'x' - open for exclusive creation, will raise FileExistsError if the file already exists

# * 'xb' - open for exclusive creation writing mode in binary. The same as x except the data is in binary.

# * 'x+' - reading and writing mode. Similar to w+ as it will create a new file if the file does not exist. Otherwise, will raise FileExistsError.

# * 'xb+' - writing and reading mode. The exact same as x+ but the data is binary

# *                       r r+ w w+ a a+
# * Read                  ✔ ✔ ✘ ✔ ✘ ✔
# * Write                 ✘ ✔ ✔ ✔ ✔ ✔
# * Creates file          ✘ ✘ ✔ ✔ ✔ ✔
# * Erases file           ✘ ✘ ✔ ✔ ✘ ✘
# * Initial position      S S  S S E E    (S-Start, E-End)

with open('016_FIles_Folders_IO/test.txt', 'r') as f:
    f.read()
with open('016_Files_Folders_IO/test.txt', 'w') as f:
    f.write("Hello")
with open('016_Files_Folders_IO/test.txt', 'a') as f:
    f.write('\n' + "Mom!!")

try:
    with open("016_Files_Folders_IO/test.txt", "x") as fout:
        pass
        # Work with your open file
except FileExistsError:
    print("File Exist")
    # Your error handling goes here
