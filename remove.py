import shutil
import os
import memory_profiler as mp
mylist = []
myremovedFl = []

#print(os.listdir())
def remove_empty_Folder_Files():
    count_files = 0
    count_folders = 0
    # if you want to remove fodlers and files empty in other path just enter your path like '/home/hp/Desktop/myfolder' here : 
    # os.chdir('/home/hp/Desktop/myfolder' )
    
    for dirpath, dirname, filename in os.walk('.'):     
        try:
            for di in dirpath:
                os.chdir(di)
                for dirpath, dirname, filename in os.walk('.'):
                    
                    if not dirname and not filename : # if you want to remove folders pycache add this : or os.path.basename(dirpath) == '__pycache__':
                        os.removedirs(dirpath)
                        #shutil.rmtree(dirpath)
                        count_folders += 1
                        myremovedFl.append(dirpath)
                    elif filename or dirname :
                        for f in filename:
                            full_path = os.path.join(dirpath, f)
                            
                            if os.stat(full_path).st_size == 0 :
                              
                               if os.path.dirname(full_path) != '.' and os.path.dirname(full_path) not in myremovedFl:
                                  myremovedFl.append(os.path.dirname(full_path))
                                  count_folders +=1 
                               os.remove(full_path)
                               count_files += 1
                               mylist.append(full_path)
                 
                    
            print(f'{count_folders} folders has removed  : {myremovedFl} \n and {count_files} files has removed : {mylist}')
        except:
            continue
print(f"Memory usage before function: {mp.memory_usage()} MB")
remove_empty_Folder_Files()
 
print(f"Memory usage after: {mp.memory_usage()} MB")
