
# ~ Unlike other languages, Python doesn't have a do-until or a do-while construct (this will allow code to be executed once before the condition is tested. However, you can combine a while True with a break to achieve the same purpose

a = 8
while True:
    a = a-1
    print(a)
    if a < 7:
        break
print('Done.')
