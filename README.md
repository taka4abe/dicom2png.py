# dicom2png.py
changing dicom files to png/jpg image. some options: 8-/16-bit, gray scale/RGB, 64/128/256/512 resolution.

help: -h


description:

copying all dicom image files in current directory tree to new dir, named 'new_dir', and chainge these files into png or jpg. DEFAULT: png, 8-bit (0-255) RGB color scale image with 256x256 matrix. 

this code depending on 
  pydicom, glob, numpy, shutil, time and PIL.

usage='dcm2png.py [options]
    

説明文:
current dir 以下に存在するすべての DICOM ファイルを新規ディレクトリー "new_dir" にコピーした上で、png や jpg image file に変換します。
オプションを使わない場合、デフォルトで pngファイル、8-bit（濃度・信号・エコー輝度 etc...: 0-255）, RGB, 256x256 マトリックスに変換します

このコードは、以下のライブラリに依存しています。
  pydicom, glob, numpy, shutil, time and PIL.

ヘルプ: -h
