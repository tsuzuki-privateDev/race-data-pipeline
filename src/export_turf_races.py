import sqlite3
import pandas as pd


def main():
    try:
        # DBに接続
        conn = sqlite3.connect("netkeiba_results.sqlite")

        # SQLでデータ抽出
        query = """
        SELECT
            race_id,
            race_date,
            course_name,
            surface,
            distance
        FROM races
        WHERE surface = '芝'
        ORDER BY distance DESC
        LIMIT 100
        """

        # pandasで取得
        df = pd.read_sql(query, conn)

        # 確認
        print("取得件数:", len(df))
        print(df.head)

        # CSV出力
        output_path = "outputs/turf_races_long_distance.csv"
        df.to_csv(output_path, index=False, encoding="utf-8-sig")

        print(f"CSV出力完了: {output_path}")

    except Exception as e:
        print("エラーが発生しました", e)

    finally:
        conn.close()


if __name__ == "__main__":
    main()
