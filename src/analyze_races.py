import sqlite3
import pandas as pd


def main():
    try:
        conn = sqlite3.connect("netkeiba_results.sqlite")

        query = """
        SELECT
            race_id,
            race_date,
            course_name,
            surface,
            distance
        FROM races
        WHERE surface = '芝'
            AND distance >= 1600
        """

        df = pd.read_sql(query, conn)

        print("取得件数：", len(df))
        print(df.head())

        # 競馬場ごとのレース数をカウント
        summary_df = (
            df.groupby("course_name")  # 競馬場ごとにグループ化
            .size()  # 件数カウント
            .reset_index(name="race_count")  # DataFrameに戻す
            .sort_values("race_count", ascending=False)  # 多い順
        )

        print("集計結果：")
        print(summary_df.head())

        output_path = "outputs/turf_1600m_race_sumamry.csv"
        summary_df.to_csv(output_path, index=False, encoding="utf-8-sig")

        print(f"CSV出力完了： {output_path}")

    except Exception as e:
        print("エラーが発生しました：", e)

    finally:
        conn.close()


if __name__ == "__main__":
    main()
