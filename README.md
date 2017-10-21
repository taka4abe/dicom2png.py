# dicom2png.py

usage: dcm2png.py [options]  
  
change all dicom image file in the "./renamed" directory tree. The name of new  
target dir is png or jpg. DEFAULT: png, 8-bit (0-255) RGB image with 256x256  
matrix (256x256x3 image channel). This code doesn't support color-map, only  
save gray scale image. This code depends on python3, pydicom, os, numpy,  
shutil, time and PIL.  
  
optional arguments:  
  -h, --help      show this help message and exit  
  -S, -16         use 16(sixteen)-bit scale, 0-66535. 16-bit image can only go
                  with .png, gray scale (one-channel) image.  
  -j, -jpg        change dicom to jpg  
  -g, -gray       use gray scale, one channel  
  -t, -32         save with 32x32 (Thirty-two) imaging matrix  
  -s, -64         save with 64x64 (Sixty-four) imaging matrix  
  -o, -128        save with 128x128 (One two eight) imaging matrix  
  -f, -512        save with 512x512 (Five one two) imaging matrix  
  -indir INDIR    name of dir_tree to collect dicom files, default:
                  './renamed'  
  -outdir OUTDIR  name of dir where png/jpg file is stored, default: 'png' or
                  'jpg'. If there is a directory with the same name, an error
                  occurs.  
  -v, --version   show program's version number and exit  
  
  



    


"./renamed" 以下のディレクトリの dir_tree 構造を保持したまま、全ての dicom ファイルを 
jpg はたは png に変換し、新規 dir ("jpg" または "png" ディレクトリ)に保存します。
オプションを付けない場合、8ビット、3チャンネル(RGB)の解像度 256x256 にて保存します。
カラーマップの保存には対応しておらず、全てグレースケール画像で保存します。
オプションをつけることで、16ビット、1チャンネル、異なる解像度（32x32, 64x64, 128x128, 
512x512）でも保存できます。

このコードは python3.6.1 にて動作確認しました。

このコードは、以下のライブラリに依存しています。
  pydicom, os, numpy, shutil, time and PIL.

ヘルプ: -h

オプション
※：オプションを指定しない場合 8-bit 形式の png ファイル、面内分解能 256x256, 3 channel （256x256x3）で保存します。

-S   16ビット（Sixteen）で保存します。16ビット画像は、png形式のグレースケール (1 channel 画像) となります。  
-j   jpg 形式で保存します。  
-g   チャンネル数 1 （グレースケール）で保存します。チャンネル数は(256, 256, 1)となります。このオプションを入れない場合、RGB 3チャンネルで保存し、チャンネル数は(256, 256, 3)で保存しますが、こちらもグレースケール画像になります。  
-t   面内分解能 32x32（thirty-two）で保存します。  
-s   面内分解能 64x64（sixty-four）で保存します。  
-o   面内分解能 128x128（one two eight）で保存します。  
-f   面内分解能 512x512（five one two）で保存します。  
-v   バージョンを表示します。
-indir  dicom ファイルを収集するディレクトリツリーの基点を指定します。デフォルトは './renamed'
-outdir  データを保存するディレクトリツリーを指定します。デフォルトは 'png' または 'jpg' になります。すでに同一名称のディレクトリがあるとエラーになります。
