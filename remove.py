import os
import time
import memory_profiler as mp

print(os.listdir())
def file_generator():
    count_files = 0
    count_folders = 0
    for dirpath, dirname, filename in os.walk('.'):     
        try:
            for di in dirpath:
                os.chdir(di)
                for dirpath, dirname, filename in os.walk('.'):
                    if not dirname and not filename:
                        os.removedirs(dirpath)
                        count_folders += 1
                    elif filename or dirname :
                        for f in filename:
                            full_path = os.path.join(dirpath, f)
                            if os.stat(full_path).st_size == 0 :
                               os.remove(full_path)
                               count_files += 1
            print(f'{count_folders} folders has removed \n and {count_files} files has removed')
        except:
            continue
print(f"Memory usage before function: {mp.memory_usage()} MB")
file_generator()
 
print(f"Memory usage after: {mp.memory_usage()} MB")