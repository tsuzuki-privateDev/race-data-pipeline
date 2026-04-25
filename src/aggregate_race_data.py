import sqlite3
import pandas as pd


def main():
    conn = None

    try:
        conn = sqlite3.connect("netkeiba_results.sqlite")

        query = """
        SELECT
            r.race_id,
            r.course_name,
            e.horse_id
        FROM races r
        INNER JOIN race_entries e
           ON r.race_id = e.race_id
        WHERE r.surface = '芝'
          AND r.distance >= 1600
        """

        df = pd.read_sql(query, conn)

        print("取得件数：", len(df))
        print(df.head())

        # レースごとの出走頭数を計算
        # race_idごとにhorse_idの数をカウント
        race_counts = (
            df.groupby(["race_id", "course_name"])["horse_id"]
            .count()
            .reset_index(name="horse_count")
        )

        print("レースごとの頭数：")
        print(race_counts.head())

        # 競馬場ごとの平均出走頭数
        summary = (
            race_counts.groupby("course_name")["horse_count"]
            .mean()
            .reset_index(name="avg_horse_count")
            .sort_values("avg_horse_count", ascending=False)
        )

        print("競馬場ごとの平均出走頭数：")
        print(summary)

        output_path = "outputs/avg_horse_count_by_course.csv"
        summary.to_csv(output_path, index=False, encoding="utf-8-sig")

        print(f"CSV出力完了: {output_path}")

    except Exception as e:
        print("エラーが発生しました:", e)

    finally:
        if conn is not None:
            conn.close()


if __name__ == "__main__":
    main()
