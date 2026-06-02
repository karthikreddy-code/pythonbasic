mylist = [10, 8, 9, 11, 12]
element = 11
pos = -1

for i in range(len(mylist)):
    if element == mylist[i]:
        pos = i
        break

if pos == -1:
    print(element, 'not found')
else:
    print(element, 'found at position', pos)
