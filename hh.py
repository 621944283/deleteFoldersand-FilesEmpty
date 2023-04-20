import os
print(os.environ.get('HOME'))
path= 'test/python/test.txt,test.py'
#print(os.path.basename(path))
#print(os.path.dirname(path))
x = os.path.split(path) # for split dirnames and filenames like ('test/python', 'test.txt')
print(path.split())
mylist = []
for i in path.split(','):
    filename = os.path.basename(i)
    mylist.append(filename)
print(mylist)
for g in mylist:
    x = g.index('.')
    print(g[x:])



print(os.path.splitext(path)) # for know extention like .txt or .py ...