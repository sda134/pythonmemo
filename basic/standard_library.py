
import sys              # システムパラメータと関数を扱う

print('- sys.path\n%s\n' % sys.path)            # ライブラリ検索の対象となるディレクトリのリストを返す
print('- sys.copyright\n%s\n' % sys.copyright)  # インタプリタの著作権を表示する


# 複合的な置き換え translate
price_str="￥1,234"
table = {
    '￥': '',
    ',': ''}
price = int(price_str.translate(table))