#!/usr/bin/env python
#coding: UTF-8

import tkinter
root = tkinter.Tk()

def clicked():
    print('button clicked')
    
button = tkinter.Button(root, text='test', command =clicked)
button.grid()        # buttonの有効化？

root.mainloop()      # GUI スレッドでメッセージループする感じ

print ('hello world')
