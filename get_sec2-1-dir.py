# -*- coding: utf-8 -*-
import argparse, os, shutil
parser = argparse.ArgumentParser(description=''' ''')
parser.add_argument('target_word', action='store',
                    help=': target word to detect and store.  ')
parser.add_argument("-i", nargs= 1, action = "store",
                    help=""": the name of the data-file (in_file).
                    default: './data_list.csv'  """)
parser.add_argument("-o", nargs= 1, action = "store",
                    help=""": name of file to save the result (out_dir).
                    default: str("./datalist" + target_word).  """)
parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.1, Oct/21/2017')
args = parser.parse_args()

print(args.target_word)
try:
    in_file = args.i[0]
except:
    in_file = './png-name_list.csv'
print("in_file is:", in_file)
try:
    out_dir = args.o[0]
except:
    out_dir = "datalist_" + args.target_word
print("out_dir is:", out_dir)

os.mkdir(out_dir)
f_read = open(in_file, 'r')
os.chdir(out_dir)

save_file = out_dir + ".csv"
f_save = open(save_file, 'w')
save_list = []
total, n = 0, 0

for x in f_read:
    if args.target_word in x:
        x = x.replace('\n', '')
        save_list.append(x)
        total += 1
f_read.close()

save_list.sort()
for x in save_list:
    f_save.write(str(x) + "\n")
    n += 1
    print("now copying", x, "{0}/{1}".format(n, total))
    one, two, three = x.split("_", 2)
    src = "../" + one + "_" + two + "/" + three
    dst = "./" + one + "_" + two + "/" + three
    shutil.copytree(src, dst)
f_save.close()

print('finished!')
