import os
import filecmp
import timeit
from time import sleep

if __name__ == '__main__':
    start = timeit.default_timer()
    walk_dir = '/Users/lupakgabor/Documents/duplicate_test/' 
    all_files = {}
    duplicated_found = False;
    for root, subdirs, files in os.walk(walk_dir):
        for file in files:
            if file not in all_files:
                all_files[file] = []
                all_files[file].append(root + '/' + str(file))
            else:
                new_files = []
                for duplicated_file in all_files[file]:
                    temp_path = root + '/' + str(file)
                    os.stat(duplicated_file)
                    os.stat(temp_path)
                    if filecmp.cmp(duplicated_file, temp_path):
                        duplicated_found = True;
                        print('Duplicated file found:')
                        print(duplicated_file)
                        print(temp_path+' DELETED')
                        os.remove(temp_path)
                    else:
                        new_files.append(temp_path)
                all_files[file] = all_files[file] + new_files
    if not duplicated_found:
        print('Duplicated files not found')
    print("END")
    stop = timeit.default_timer()
    m, s = divmod(stop - start, 60)
    h, m = divmod(m, 60)
    print ("%d:%02d:%02d" % (h, m, s))
    