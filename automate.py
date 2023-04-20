import os

from datetime import datetime
#print(dir(os))

#print(os.getcwd())
#os.chdir('Test/test')
#print(os.getcwd())
#print(os.listdir())
#os.mkdir('Code')

#os.makedirs('Test/test')
x = os.listdir()

#os.mkdir('Code')
#os.removedirs('Test/test')
#os.makedirs('code')
""" try :
    os.chdir('code')
    g = os.listdir()
    if len(g) == 0 :
      os.chdir('..')
      os.rmdir('code')
    elif len(g) > 0 :
       os.chdir('..')
       for i in g :
          os.rmdir(f'code/{i}')
except :
   pass
print(os.getcwd()) """

#o = os.stat('hh.py').st_size
#p = datetime.fromtimestamp(o)
#print(os.stat('hh.py').st_size)
#print(datetime.fromtimestamp(os.stat('hh.py').st_atime))
#os.remove('cf.txt')
#os.rename('haha','code')

#for dirpath,dirnams,filenames in os.walk('.'):
#    print(dirpath,dirnams,filenames)
#print(os.environ.get('HOME'))
path= 'Test/test/hg.txt'
#print(os.path.basename(path))
#print(os.path.dirname(path))
#print(os.path.split(path)) # for split dirnames and filenames like ('test/python', 'test.txt')
#print(os.path.splitext(path)) # for know extention like .txt or .py ...
f = os.listdir()
print(f)
#for i in f :
    #print(os.path.isfile(i))
    #print(os.path.isdir(i))
    #pass
print(os.path.exists(path))

