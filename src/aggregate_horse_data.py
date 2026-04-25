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

        horse_race_count = (
            df.groupby("horse_id")["race_id"]
            .count()
            .reset_index(name="race_count")
            .sort_values("race_count", ascending=False)
        )

        print("馬ごとの出走回数：")
        print(horse_race_count.head())

        output_path = "outputs/horse_race_count.csv"
        horse_race_count.to_csv(output_path, index=False, encoding="utf-8-sig")

    except Exception as e:
        print("エラーが発生しました:", e)

    finally:
        if conn is not None:
            conn.close()


if __name__ == "__main__":
    main()
