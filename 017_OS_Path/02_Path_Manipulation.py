import os

p = os.path.join(os.getcwd(), 'foo.txt')
print(p)
print(os.path.dirname(p))
print(os.path.basename(p))
print(os.path.split(os.getcwd()))
print(os.path.splitext(os.path.basename(p)))
