import os 

count = 0
for dirpath,dirname,filename in os.walk('.'):
   try :

      for di in dirpath :
          os.chdir(di)
          for dirpath,dirname,filename in os.walk('.'):
              if not dirname and not filename :
                os.removedirs(dirpath)
                count += 1
              if filename :
                 print(filename)
      
      print(count)
      
   except :
       continue
#print(os.stat('hh.py').st_size)