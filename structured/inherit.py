
# 先に継承時の注意点！

class BaseTestClass():    #基底クラス（親クラス，スーパークラス）
    __str_val = 'base!'
    percentage = 0.10           
    def __init__(self, int_val, str_val):
        self.__int_member = 0           # __init__ で生成したprivate(__ではじまる)メンバは，派生クラスではアクセスもできない
        self.title = 'base title!'

    def what_is_intval(self):
        print(self.__int_member)

    def what_is_strval(self):
        print(self.__str_val)

    def what_is_title(self):
        print(self.title)

    def what_is_percentage(self):
        print(self.percentage)


class InheritTestClass(BaseTestClass): # 継承クラス（子クラス，サブクラス）
    def __init__(self, int_val, str_val):
        super().__init__(int_val, str_val)  # スーパークラスのinitialiser を呼び忘れないように
        self.__int_member = int_val
        self.__str_val = 'super!'           # これは本クラスの値を変更するだけ
        self.title = 'super title!'         # これは基底クラスの値も変更する
        self.percentage = 20.0


sp_cls = InheritTestClass(36, "hoge")
sp_cls.what_is_strval()             # base クラスの値を printする。どうやら各クラスのprivate変数にしてしまうと
                                    # _BaseTestClass__str_val と self._BaseTestClass__str_valとなり，全く別の変数になる
sp_cls.what_is_title()              # private でなければ，__init__で生成しようが，class の直後で生成しようが
sp_cls.what_is_percentage()         # 普通にアクセスできるらしい。
#sp_cls.what_is_intval()            # これはエラーになる　has no attribute '_BaseTestClass__int_member'

# ⇒ 継承関係にある時でも，private 変数にアクセスする時には getter/setter が必用と言う事。
# method でも良いが，python はproperty が作れるので，property の方が無難。


