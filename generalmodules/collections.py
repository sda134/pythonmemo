
    # ホストとメッセージの組み合わせをキーにしたCounterを作成
    counter = Counter((record["hostname"], record["message"]) for record in record_list)

    # 結果を表示
    for key, count in counter.items():
        host, message = key
        print([host, message, count])

https://docs.python.org/ja/3/library/collections.html