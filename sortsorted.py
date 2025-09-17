from operator import index

a = ['apple', 'orange', 'banana', 'pear', 'kiwi']
print(sorted(a,key=lambda x:x[-1]))  # Sort by last letter
print(sorted(a,key=lambda x:x[0]))   # Sort by first letter
print(sorted(a,key=lambda x:len(x))) # Sort by length of the string
print(sorted(a,key=lambda x:x))      # Sort alphabetically
print(sorted(a,key=lambda x:-len(x)))# Sort by length of the string in reverse
print(sorted(a,key=lambda x: a.index(x))) # Sort by index in reverse