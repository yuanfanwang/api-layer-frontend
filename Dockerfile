# ベースイメージ
FROM python:3.9-slim

# 作業ディレクトリの設定
WORKDIR /app

# 必要なファイルをコピー
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# アプリケーションを起動
CMD ["python", "app.py"]

# ポート5000を公開
EXPOSE 5000