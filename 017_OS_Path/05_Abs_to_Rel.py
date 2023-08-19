import os

print(os.getcwd())
print(os.path.abspath("./"))  # D:\Programming\Python
print(os.path.abspath("../../../"))
print(os.path.abspath("016_Files_Folders_IO/test.txt"))
# D:\Programming\Python\016_Files_Folders_IO\test.txt
print(os.path.abspath("/016_Files_Folders_IO/test.txt"))
# D:\016_Files_Folders_IO\test.txt
