#!/usr/bin/env python
#coding: UTF-8

# ある package にあったので真似をしてみたが、あまり使われている例を見たことがない。20.03.02
# python の package に必須のファイルと誤解されてしまうので、__main__.py というファイル名はむしろ控えるべき
#
# core.py だったり main.py だったりファイル名が作者により異なるが，
# C言語系の void main(int argc, char *argv[] ){} みたいにエントリポイントとして使い、
# c++ の.h(ヘッダー) の様にメインメソッド群を見通し良く記述すると良い様に思う 20.03.25

print("mypackage__main__.py is loaded! from __main__.py")

class MyClass():
    def say_myname(self):
        print('say_myname:MyClass!!')
