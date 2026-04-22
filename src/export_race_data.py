import sqlite3
import pandas as pd

# DBに接続
conn = sqlite3.connect("netkeiba_results.sqlite")

# SQLでデータ取得
query = """
SELECT race_id, course_name, distance
FROM races
LIMIT 100
"""

df = pd.read_sql(query, conn)


# 簡単に加工する
def distance_category(d):
    if d <= 1400:
        return "短距離"
    elif d <= 1800:
        return "マイル"
    else:
        return "中長距離"


# 距離(distance)を基にレース種別（短距離・マイル・中長距離）へ分類する
df["distance_category"] = df["distance"].apply(distance_category)

# CSV出力
df.to_csv("outputs/race_sample.csv", index=False, encoding="utf-8-sig")

# 接続を閉じる
conn.close()

print("完了")
