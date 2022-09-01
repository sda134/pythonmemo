import argparse

'''
実行方法
python3 main.py hoge fuga --number 2
>> model:hoge label:fuga number:2
'''

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('model', help='説明文')
    parser.add_argument('--number', type=int, default=3)
    args = parser.parse_args()
    print('model:%s number:%s' % (args.model, args.number))


# parser.add_argument('arg', help='説明')	# 説明の文字列を指定
# >> python3 main.py –h				        # このようにすると表示される
# parser.add_argument('arg', type=str)		# データ型の指定
# parser.add_argument('arg', nargs='*')		# 複数の引数の指定
# parser.add_argument('arg', nargs='+')		# 複数の引数の指定（１つ以上強制）
# parser.add_argument('--option')		    # オプション引数
# parser.add_argument('-o', '--option')		#　省略形オプション
