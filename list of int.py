'''
Write a Python program to filter a list of integers using Lambda.
'''
l=[1,3,42,5,4,32]
p=filter(lambda s:s>10,l)
print(list(p))