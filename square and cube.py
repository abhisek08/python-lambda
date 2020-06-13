'''
Write a Python program to square and cube every number in a given list of integers using Lambda.
'''
l=[1,2,3,4]
s=map(lambda s:s**2,l)
print(list(s))
s=map(lambda s:s**3,l)
print(list(s))