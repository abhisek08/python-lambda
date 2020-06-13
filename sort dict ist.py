'''
Write a Python program to sort a list of dictionaries using Lambda.
'''
l=[{1:1,2:2},{0:0,1:1}]
l.sort(key=lambda x:x.get(1))
print(l)