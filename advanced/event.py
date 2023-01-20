class EventClass():
    def __init__(self):
        self.sample_event=None
    def loop_proc(self):
        # 実際には concurrent.futures の ThreadPoolExecutor などを使う
        self.sample_event('hoge', 123)




