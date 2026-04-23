import sqlite3
import pandas as pd


def main():
    try:
        conn = sqlite3.connect("netkeiba_results.sqlite")

        query = """
        SELECT
            r.race_id,
            r.race_date,
            r.course_name,
            r.surface,
            r.distance,
            e.horse_id,
            e.horse_name
        FROM races AS r
        INNER JOIN race_entries AS e
            ON r.race_id = e.race_id
        WHERE r.surface = '芝'
            AND r.distance >= 1600
        ORDER BY r.race_id DESC, r.race_id ASC, e.horse_id ASC
        LIMIT 200
        """

        df = pd.read_sql(query, conn)

        print("取得件数：", len(df))
        print(df.head(10))

        output_path = "outputs/joined_races_and_entries.csv"
        df.to_csv(output_path, index=False, encoding="utf-8-sig")

    except Exception as e:
        print("エラーが発生しました")

    finally:
        conn.close()


if __name__ == "__main__":
    main()
