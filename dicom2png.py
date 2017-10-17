# -*- coding: utf-8 -*-
import argparse, os, dicom, shutil, time
from PIL import Image
import numpy as np

parser = argparse.ArgumentParser(
    description='''change all dicom image file in this directory tree to
    png or jpg. DEFAULT: png, 8-bit (0-255) RGB image with 256x256 matrix (256x256x3 image channel).
    This code depends on python3, pydicom, os, numpy, shutil, time and PIL.''',
    usage='dcm2png.py [options]')
parser.add_argument('-d', '-16', action='store_true',
                    help='use 16(hexa-Deca)-bit scale, 0-66535. 16-bit image can only go with .png, gray scale image.') # オプションを追加します
parser.add_argument('-j', '-jpg', action='store_true',
                    help='change dicom to jpg') # オプションを追加します
parser.add_argument('-g', '-gray', action='store_true',
                    help='use gray scale, one channel') # オプションを追加します
parser.add_argument('-t', '-32', action='store_true',
                    help='save with 32x32 (Thirty-two) imaging matrix') # オプションを追加します
parser.add_argument('-s', '-64', action='store_true',
                    help='save with 64x64 (Sixty-four) imaging matrix') # オプションを追加します
parser.add_argument('-o', '-128', action='store_true',
                    help='save with 128x128 (One two eight) imaging matrix') # オプションを追加します
parser.add_argument('-f', '-512', action='store_true',
                    help='save with 512x512 (Five one two) imaging matrix') # オプションを追加します
parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.1') # version
args = parser.parse_args() # コマンドラインの引数を解釈します

start = time.time()
data_type, reso = ['8-bit', 'png', 'RGB'], 256

if args.d:
    data_type[0, 1, 2] = '16-bit', 'png', 'gray_scale'
elif args.j:
    data_type[1] = 'jpg'
elif args.g:
    data_type[2] = 'gray_scale'
if args.t:
    reso = 32
if args.s:
    reso = 64
elif args.o:
    reso = 128
elif args.f:
    reso = 512

print('changing dicom to data type:', data_type)
n, total, sequence_list = 0, 0, []
target_dir = '.' # defaul target directory

for root, dirs, files in os.walk(target_dir):
    for file_name in files:
        try:
            file_name_, ext = os.path.splitext(file_name)
            if ext == '.dcm':
                total += 1
            else:
                pass
        except:
            pass

print('total of {} dicom files'.format(total))

if os.path.exists('new_dir'):
    print("Error!!   Directory 'new_dir' has already existed.")
    print("Program finished")
else:
    pass

shutil.copytree(target_dir, 'new_dir')
check_point = time.time()

for root, dirs, files in os.walk('new_dir'):
    for file_name in files:
        try:
            file_name_, ext = os.path.splitext(file_name)
            if ext == '.dcm':
                file_path = root + "/" + file_name
                try:
                    ds = dicom.read_file(file_path)
                    pix = ds.pixel_array
                    if data_type[0] == '16-bit':
                        pix = ((pix / np.max(pix)) * 65535).astype(np.uint16)
                        pix = pix.astype(np.uint16)
                        #
                        save_name = root + "/" + file_name_ + ".png"
                        Image.fromarray(np.uint16(pix)).convert('L').resize(
                            (reso, reso), Image.LANCZOS).save(save_name)
                    else: #data_type[0] == '8-bit'
                        pix = ((pix / np.max(pix)) * 255).astype(np.uint8)
                        if data_type[1] == 'jpg':
                            save_name = root + "/" + file_name_ + ".jpg"
                        else: #elif data_type[1] == 'png':
                            save_name = root + "/" + file_name_ + ".png"
                        if data_type[2] == 'gray_scale':
                            Image.fromarray(pix).convert('L').resize(
                                (reso, reso), Image.LANCZOS).save(save_name)
                        else: #elif data_type[2] == 'RGB':
                            tmp_reso = [pix.shape[0], pix.shape[1]]
                            pix = np.reshape(pix, (tmp_reso[0]*tmp_reso[1], 1))
                            pix2 = np.append(pix, pix, axis = 1)
                            pix = np.append(pix2, pix, axis = 1)
                            pix = np.reshape(pix, (tmp_reso[0], tmp_reso[1], 3))
                            Image.fromarray(np.uint8(pix)).convert('L').resize(
                                (reso, reso), Image.LANCZOS).save(save_name)
                    os.remove(file_path)
                except:
                    pass
            else:
                pass
        except:
            pass

        n += 1
        if n == 10 or n == 20 or n == 50 or n% 100 == 0:
            elapsed_time = time.time() - check_point
            print("{0} / {1} cases processed,  elapsed time: {2:2.02f} sec".format(n, total, elapsed_time))
            print("{0:2.02f} sec to finish converting".format(((elapsed_time/n)*total)-elapsed_time))
            print(' ')

elapsed_time = time.time() - start
print("{0} cases processed with {1} sec.".format(n, elapsed_time))
print("Finished!!")
