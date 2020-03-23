#!/usr/bin/env python
#coding: UTF-8

# https://qiita.com/Usek/items/a206b8e49c02f756d636
# クラスの書き方

"""
doctext
クラスの説明をここに書く
参考資料：https://docs.python.org/ja/3.6/reference/datamodel.html#index-34
"""

class TestClass():
    def __init__(self, arg1=0):     # コンストラクタ ※デフォルト値を持っているのでオーバーロードのように扱える
        print('initialiser invoked!') # __init__ だからか、initializer と呼ぶ人もいる。
        self.__value = 1            # これでもメンバが生成される(private)
        self.Field = "PublicField"  # これでもメンバが生成される(public)
                                    # 基本的には init のオーバーロードは不可。継承などで対応する。

    def __del__(self):              #デストラクタ
        print('destructor invoked!')

    @classmethod
    def ClassMethod(cls):              # static method のようにインスタンス化しなくても使える
        print('this is class method!')  # 第一引数は、本クラスのインスタンス。慣例としてclsとするが、名前は自由。
        return cls                      # インスタンスの使える静的メソッド、といった所
    

    def sample_method(cls):          # あまり使わない方が良いらしいが、
        return cls                    # こういった方法もある
    sample_method = classmethod(sample_method)


    @staticmethod
    def StaticMethod():                # static method 
        print('this is static method!')# インスタンスを使用しない（使用できない）メソッド

    @property                       # プロパティ get
    def comment(self):
        return self.__comment
    @comment.setter                 # プロパティ set
    def comment(self, arg):    
        self.__comment = arg

    def __privatePrint(self):       # 疑似 private    
        print('this is supposed to be private...')  # hoge._ClassName__methodname() でアクセスできてしまう（非推奨）

    @classmethod
    def __private_class_method(cls):                # python に完全なprivate は存在しない。
        print('this is supposed to be private...')  # hoge._ClassName__methodname() でアクセスできてしまう（非推奨）
        return cls



    def PublicPrint(self, arg :str): # パブリックメソッド（＋引数のヒント　注意！型指定ではない）
        if not isinstance(arg, str):
            raise ValueError('the arg must be str') # 確実に str型が欲しいならこのようにするしかない。
        return "This is Public Method! arg:%s" % arg

    # --- 特殊メソッド --- 
    def __str__(self):                          # toString() の様な物。printなどで文字列に変換する場合に呼び出される。
        return "__str__"

    def __repr__(self):                         # __str__ に似ているが、repr() を使った時の結果
        return "__repr__"

    def __hash__ (self):                        # Hash値を返す。オブジェクトを示す、唯一無二、一意な値。
        return 0

    def __dir__(self):
        print('__dir__ is called!!')            # 本インスタンスに対して dir()  された時に呼び出される


    def __bytes__(self):                        # 文字通り。バイナリのバイトデータを返す。
        return bytearray([0x00, 0x00])

    def __format__(self, format_spec):          # format_spec に準じた文字列　？？__str__とどう違う？
        return self.__str__
    
    def __bool__(self):                         # 使う機会があるのだろうか？
        return True


    def __enter__(self):                        # with 用：使用時によびだされる
        print("for with - enter")
        return self    
    def __exit__(self, type, value, traceback):# with 用：終了時によびだされる
        print("for with - exit")


    def __iter__(self):                         # イテレータ forループなどで使う　C#などのコレクションで使用？
        return iter(['iter1','iter2'])
    def __next__(self):                         # __iter__と共に使う。
        return None

    def __call__(self):
        print('did someone call me?')           # 本クラスをメソッドのように呼び出した時に実行される。利用価値ある？

    def __add__(self, other):                   # + で足し算する時のメソッド　operator+ みたいな
        pass
    def __setattr__(self, name, value):         # = が使われた時に呼び出される。operator= みたいな
        self.__dict__[name] = value
        pass
    def __getattr__(self, value):               # __setattr__ のget版
        pass


    """
    メソッドの説明をここに書く
    """
    def StringMethod(self) -> str:   # 戻り値の型ヒント　注意！型指定ではない
        return "string method!"


def say_hello():
    print('hello from class_samples')



# ------ 以下、検証
ts = TestClass()
ts.comment = 'hogegehogege'
print(ts.StringMethod())
TestClass.StaticMethod()     # static method の実行
hoge =TestClass.ClassMethod()
print('\n' + '-' * 30)


print('excute of private method')       # python にはprivate の概念がない
ts._TestClass__privatePrint()           # このようにすると実行できてしまう（非推奨）
ts._TestClass__private_class_method()   # class method 版
print('\n' + '-' * 30)                  


# イテレータの検証
for iterItem in ts:
    print('iter item: %s' % iterItem)

print(type(ts))                  # 型の情報を表示
print(isinstance(ts, TestClass)) # 型の確認方法
