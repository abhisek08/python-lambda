'''
Write a Python program to sort a list of tuples using Lambda.
'''
l=[(1,2,3),(4,5,6),(0,1)]
l.sort(key=lambda x:x[1])
print(l)