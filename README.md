# race-data-pipeline

競馬データ（netkeiba）を取得・加工し、分析用データを生成するパイプライン

## 📌 概要
- レースデータの収集
- データベース（SQLite）への保存
- pandasによるデータ加工
- CSV出力

## 🛠 使用技術
- Python
- SQLite
- pandas
- BeautifulSoup

## 📂 ディレクトリ構成
- src/ : 本番コード
- notebooks/ : 分析用
- outputs/ : 出力データ

## 🚀 今後の予定
- データの自動更新（バッチ化）
- 特徴量作成の強化
- API化