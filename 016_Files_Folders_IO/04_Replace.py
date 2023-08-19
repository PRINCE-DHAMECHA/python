import fileinput

# * Replaces Hello with Hey and Mom with Mother if it's there in file
replacements = {'Hello': 'Hey',
                'Mom': 'Mother'}
for line in fileinput.input('016_Files_Folders_IO/test.txt', inplace=True):
    for search_for in replacements:
        replace_with = replacements[search_for]
        line = line.replace(search_for, replace_with)
    print(line, end='')
