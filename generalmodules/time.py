import time

for i in range(5):
    time.sleep(0.01)        # sleep関数の引数は float
    print(dt.now())
print('')



print('time.time')          # UNIX時間（エポック秒）の表示
for i in range(5):          # 　協定世界時 (UTC) での1970年1月1日午前0時0分0秒
    print(time.time())      # 　からの経過秒数。
print('')


print('time.gmtime')        # 協定世界時 で表示
for i in range(5):
    print(time.gmtime())


print('time.perf_counter')
# 時間を測るデコレータ関数
def method_timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()                # 時間を測り始める
        result = func(*args, **kwargs)
        duration = time.perf_counter() - start_time      # 終了時間 - 開始時間でかかった時間を計測
        print(f"func:{func.__name__}\ttime: {duration: .5f} sec")
        return result
    return wrapper

@method_timer
def some_heavy_task():
    time.sleep(5)

some_heavy_task()
