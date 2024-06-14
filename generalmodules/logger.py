# coding:utf-8
# 標準出力とテキストファイルの両方にログを出力する例

# ログのライブラリ
import logging
from logging import getLogger, StreamHandler, FileHandler, Formatter

#rootロガーを取得
logger = getLogger()
# 全体のレベルを設定
logger.setLevel(logging.DEBUG)

# handlerの生成(file)
file_handler = FileHandler(filename='log.txt', encoding='utf-8')
file_handler.setLevel(logging.INFO)
# ログ出力フォーマット設定(file)
file_handler_format = Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_handler_format)
# ハンドラーをセット(file)
logger.addHandler(file_handler)


# handlerの生成(stream)
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
# ログ出力フォーマット設定(stream)
streame_handler_format = Formatter('%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(streame_handler_format)
# ハンドラーをセット(stream)
logger.addHandler(stream_handler)