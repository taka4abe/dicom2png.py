# dicom2png.py
changing dicom file to png/jpg image. some options: 8-/16-bit, gray scale/RGB, 64/128/256/512 resolution

help: -h


copying all dicom image file in this directory tree to new dir, named 'new_dir', and chainge these files into png or jpg. DEFAULT: png, 8-bit (0-255) gray scale image with 256x256 matrix. 

this code depending on 
  pydicom, glob, numpy, shutil, time and PIL.

usage='dcm2png.py [options]
    

説明文
current dir 以下に存在するすべての DICOM ファイルを新規ディレクトリー "new_dir" にコピーした上で、png や jpg image file に変換します。

このコードは、以下のライブラリに依存しています。
  pydicom, glob, numpy, shutil, time and PIL.

ヘルプ: -h
