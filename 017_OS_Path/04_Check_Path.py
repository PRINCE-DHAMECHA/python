import os

# * Check path if exist or not
path = './017_OS_Path'
print(os.path.exists(path))  # True
# this returns false if path doesn't exist or if the path is a broken symbolic link

# * check if the given path is a directory, file, symbolic link, mount point etc

dirname = './016_Files_Folders_IO'
print(os.path.isdir(dirname))

filename = os.path.join(dirname, 'test.txt')
print(filename)
print(os.path.isfile(filename))

# * to check if the given path is symbolic link
# symlink = dirname + 'some_sym_link'
# os.path.islink(symlink)

# * to check if the given path is a mount point
mount_path = '/'
print(os.path.ismount(mount_path))
