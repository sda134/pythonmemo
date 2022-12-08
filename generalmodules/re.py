import os
import re

# ファイル名リスト
file_list = os.listdir(dir_from)

# イメージファイルのリスト
xml_file_list = filter(lambda arg: re.search(".png$|.jpeg$|.jpg$", arg), file_list)