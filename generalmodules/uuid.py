import uuid


# https://docs.python.org/ja/3/library/uuid.html

# ホスト ID、シーケンス番号、現在時刻から生成
print(uuid.uuid1)

# 完全にランダムなuuidを発行
print(uuid.uuid4)

