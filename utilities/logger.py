#!/usr/bin/env python
#coding: UTF-8

# 初めに：
# ・print() もログを残す手段としては有効だが、積極的に loggerクラスで作成したインスタンスを使うべき。
#  理由：python 標準の書き方に倣う事で、他の人にライブラリを使ってもらった時に役立つし、
#       他の人がログを見た時に理解してもらいやすい。
#
# logging.debug() など、インスタンスを仲介しないルートロガーの例をよく見かけるが、するべきではない。
# 理由：ロガーの構造、python 標準の logging クラスの概要が理解しにくい為。
# 参考資料：http://pieces.openpolitics.com/2012/04/python-logging-best-practices/（英語）
# 
# ほとんどの logger インスタンスにはレベルのセットはせず default の WARNING 以上を用いるべきである。


# ここでは、以下のように log を出力する
# ・warning 以上はテキストファイルに出力
# ・それ未満は Console に出力
# ・critical はemail を送信


import logging
# ↓ モジュール名 logging と変数名 logger が紛らわしいので、
# ↓ 下のような import がベスト、と言う意見も。⇒ 紛らわしい変数名はやめれば？？
# from logging import getLogger, StreamHandler, DEBUG, CRITICAL

# 同フォルダの logging.conf を設定ファイルとして利用できる
import logging.config

# SMTPHandler などを使う場合はこちらも import
import logging.handlers


# 通常は class 名などが入る。ここでは仮の値を入れておく。
__name__ = 'logger_sample'


# Logger, Formatter, Handler, Filter がロガーの４大要素らしい

# Logger：ロギングシステムにメッセージを送る
# 「ルートロガー」を基に、ツリー上にロガーが作成されるらしい
# 下の様に、引数に名前を入れてロガーを作成する。特定の　module に特化したロガーを作成。
logger = logging.getLogger(__name__)

# ※すべての moludle にそれぞれの名前付き logger を持たせ、１対にすべき
# 当然、名前もパッケージ/モジュール階層にして、よびだしたモジュールが明確になるようにする（以下のどちらかを使用する）
child_logger1 = logging.getLogger('parent.child')
child_logger2 = logging.getLogger(__name__).getChild('child')

# 引数なしでルートロガーになるが、利用する事はほぼ無い __name__ = 'root'
root_logger = logging.getLogger()


# logger の設定　※但し、全Loggerに適用されてしまうので、個々のlogger に設定を入れた方が良い
logging.basicConfig(
    # level=logging.DEBUG,    # ※ここでのレベル設定は行わない！logger.setLevel() を用いる事！ 
    # filename='example.log',   # ファイルに出力する　複数ファイル(.py) から呼び出して、同じファイルへの出力が可能
    # format='%(asctime)s %(levelname)-8s %(module)-18s %(funcName)-10s %(lineno)4s: %(message)s'
    )

# 明示的に logging.conf を使用する
'''
logging.config.fileConfig(
    fname = 'logging.conf',          #
    disable_existing_loggers = True,
    )
'''

# Handler：メッセージをどこに出力するか、を定義する
logger.setLevel(logging.DEBUG)             # logger はハンドラで設定されたレベル以下にする必要がある

file_handler = logging.FileHandler('example.log', 'a')
file_handler.setLevel(logging.WARNING)     # 指定値を含む上位レベルのログのみ記録される。レベルについては後述。

smtp_handler = logging.handlers.SMTPHandler( # なぜパスワードなしでメールが送れる？
    mailhost='pop.m-tec-m.co.jp',            # mail server
    fromaddr='isaji@m-tec-m.co.jp',          # 'hoge@example.com'
    toaddrs=['isaji@m-tec-m.co.jp'],
    subject='SMTPHandlerから送信されるメールのタイトル'
)
smtp_handler.setLevel(logging.CRITICAL)




# Formatter：ハンドラが使用するフォーマットを定義する 
# 参考('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)-8s %(module)-18s %(funcName)-10s %(lineno)4s: %(message)s')
file_handler.setFormatter(formatter)


# loggerに適用：反対はLogger.removeHandler() 
logger.addHandler(file_handler)
#logger.addHandler(smtp_handler)    # メール送信されてしまうのでコメントアウト



# 記録メソッド５つ。
# ただのカテゴリ分けではあるが、一般に下に行くほど深刻で重要度が高い。
# filename の設定が無ければ Console に出力される
logger.debug('debug message')       # level = 10
logger.info('info message')         # level = 20
logger.warning('warn message')      # level = 30
logger.error('error message')       # level = 40
logger.critical('critical message') # level = 50


'''
# Filter：どの logRecord を出力するかの細かい出力制御　ほとんど使わないらしい
#mod_logger.addFilter()      # Logger.removeFilter()

logger.exception('exception message') # 例外の時にのみ使うべき

# このような記述も可能ではあるが、できるだけ使わない方よい。
# なお、ルートロガー root_logger = logging.getLogger() # これと同じになる
logging.debug('1. This is debug.')

# 変数の使用　str の format と同じ
str_look ='Look'
logging.warning('%s before you %s', str_look, 'leap!')
'''


# 便利な定義済サブクラスハンドラ
'''
logging.StreamHandler()          # メッセージをストリーム (ファイル風オブジェクト) に送る。実際にはConsoleに送る事が多い
logging.FileHandler()            # メッセージをディスクファイルに送ります。
logging.BaseRotatingHandler()    # ある地点でログファイルを循環させるハンドラの基底クラスです。これを直接インスタンス化することは意図されていません。代わりに、 RotatingFileHandler や TimedRotatingFileHandler を使用してください。
logging.RotatingFileHandler()    # メッセージをディスクファイルに送り、最大ログファイル数とログファイル循環をサポートします。
logging.TimedRotatingFileHandler() # メッセージをディスクファイルに送り、ログファイルを特定時間のインターバルで循環します。
logging.SocketHandler()          # TCP/IP ソケットにメッセージを送ります。バージョン3.4　から、 Unixドメインソケットもサポートされます。
logging.DatagramHandler()        #  UDP ソケットにメッセージを送ります。バージョン 3.4 から、Unix ドメインソケットもサポートされます。
logging.SMTPHandler()            # メッセージを指示された email アドレスに送ります。
logging.SysLogHandler()          # メッセージを、必要ならばリモートマシンの、Unix syslog daemon に送ります。
logging.NTEventLogHandler()      # メッセージを Windows NT/2000/XP イベントログに送ります。
logging.MemoryHandler()          # メッセージを、特定の基準が満たされる度に流される、メモリ中のバッファに送ります。
logging.HTTPHandler()            # メッセージを、 GET または POST セマンティクスを使って、HTTP サーバに送ります。
logging.WatchedFileHandler()     # ロギングする先のファイルを監視します。ファイルが変更されると、そのファイルは閉じられ、ファイル名を使って再び開かれます。このハンドラは Unix 系のシステムにのみ便利です。Windows は、使われている基の機構をサポートしていません。
logging.QueueHandler()           # queue モジュールや multiprocessing モジュールなどで実装されているキューにメッセージを送ります。 instances send messages to a queue, such as those implemented in the queue or multiprocessing modules.
logging.NullHandler()            # エラーメッセージに対して何もしません
'''
