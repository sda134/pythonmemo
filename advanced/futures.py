# 公式：https://docs.python.org/ja/3/library/concurrent.futures.html

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# ProcessPoolExecutor   大きめの処理
# ThreadPoolExecutor    小さめの処理

values = [100,200,300]

def task1(value:int):
  # do something

def task2(str_val:str):
  # do something

# 単純に１つの処理を行う
with ThreadPoolExecutor(max_workers=2, thread_name_prefix="thread") as executor:
    executor.submit(task, 100)          # メソッドを渡さないといけない点に注意
    executor.submit(task2, 'fuga')      # task() とすると実行結果を渡す事になってしまう


# １つのメソッドに複数の値をあたえて、そのすべてを実行する
with ThreadPoolExecutor(max_workers=2, thread_name_prefix="thread") as executor:
    for number, results in zip(executor.map(task1(), values)):
        print(number)
