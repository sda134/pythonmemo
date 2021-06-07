# !/usr/bin/env python
# coding: utf-8

# https://docs.python.org/ja/3/library/exceptions.html


try:
    print(1/0)
except ZeroDivisionError as e:
    print(e)
except Exception as e:
    print ('不明なエラー: %s' % e)
else:
    pass                       # 例外が発生しなかった場合
finally:
    # finally で return, break, continue を使わない事！
    #
    #
    pass                       # 例外が発生しようがしまいが実行される

# 例外を発生させる
input_val =int(input('数値を入力してください'))
if input_val < 0:
    raise ValueError('0未満が入力')


# KeyboardInterrupt


# ユーザー定義例外
class MyException(Exception):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self):
        #self.expression = expression
        #self.message = message
        pass
    
    def __str__(self):
        return "Hello from MyException!"


try:
    raise MyException()
except Exception as e:
    print(e)