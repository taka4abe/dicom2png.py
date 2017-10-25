# -*- coding: utf-8 -*-
# get information from png filename
# this code is thought to be used with dicom2png.py and other repositories (dcm_rename.py?).

import os, time
print('\ncode started...\n')

save_file = "data_list.txt"
f = open(save_file, 'w')
start = time.time()
total = 0
target_dir = '.'

for root, dirs, files in os.walk(target_dir):
    for file_name in files:
        total += 1
print('total of {} files\n'.format(total))

n_verbose = total // 20 + 1
n = 0
save_list = []

for root, dirs, files in os.walk(target_dir):
    for file_names in files:
        file_name, ext = os.path.splitext(file_names)
        n += 1
        if ext == ".png":
            if not file_name in save_list:
                save_list.append(file_name)
            else:
                pass
        else:
            pass
        if (n % (n_verbose//8) == 0 and n < n_verbose) or n % n_verbose == 0:
            elapsed_time = time.time() - start
            process_speed = n/elapsed_time
            print(
"{0}/{1} processed, {2:0.0f}/sec. elapsed/est_total: {3}/{4} sec \n".\
format(n, total, process_speed, int(elapsed_time), int((elapsed_time/n)*total))
                  )

save_list.sort()
for x in save_list:
    f.write(str(x) + "\n")
f.close()

print("data from {0}/{1} files were collected in {2} sec \nand saved to {3}.\n\
finished\n".format(n, total, int(time.time() - start), save_file))
