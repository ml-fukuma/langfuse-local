# Langfuse Local Setup (v2)

このリポジトリは、Langfuse v2 を macOS の Rancher Desktop 環境でローカル実行するためのセットアップガイドです。


## 🚀 前提条件

- macOS
- Rancher Desktop


## ⚙️ Rancher Desktop 設定

1. Rancher Desktop を起動
2. 左メニュー「Virtual Machine」→ Enabled（ON）
3. 「Container Runtime」→ dockerd (moby)
<img src="./img/img1.png" width="50%">

4. 動作確認コマンド
```bash
    docker version
```


## 📦 プロジェクト構成

    langfuse-local/
    ├─ docker-compose.yml
    └─ README.md


## ▶ 起動方法

    docker compose up -d

### 起動状態確認

    docker compose ps


## 🌐 ブラウザアクセス

    http://localhost:3000

### 初回ログイン

- メールアドレス：任意 (例: test@example.com)
- パスワード：任意（8文字以上）


## 🛑 停止・削除

| 操作 | コマンド |
|---|---|
| 停止（データ保持） | docker compose stop |
| 再開 | docker compose start |
| コンテナ削除（データ保持） | docker compose down |
| コンテナ＋DB完全削除 | docker compose down -v |


## 🐛 トラブルシューティング

### 起動ログ確認

    docker compose logs -f

## main.py の実行方法

Langfuse + ローカルLLMなどアプリ側が正常起動しているか確認するために、 `main.py` を直接実行できます。

### 環境変数の設定 
1. Langfuse の管理画面（Project Settings → API Keys）で発行した  
   **Public Key / Secret Key** をコピー

2. client配下の `.env` に以下内容を記述

```env
LANGFUSE_PUBLIC_KEY=lf-pub-xxxxxxxxxxxxxxxx
LANGFUSE_SECRET_KEY=lf-sec-xxxxxxxxxxxxxxxx
LANGFUSE_HOST=http://localhost:3000
```

### main.py実行
```bash
# 仮想環境に入る
cd ./client
pipenv shell
pipenv install


# 実行
python main.py
```

上記実行後に下記が出力されればOK
```bash
sent!
```

### 🔍 実行時に確認すべきポイント
http://localhost:3000 のダッシュボードにTraces数が表示されていればOKです。
<img src="./img/img-result.png" width="50%">

## 📝 ライセンス

この設定はローカル検証目的で使用可能です。
