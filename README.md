# simple-ai-hackathon4-d

このプロジェクトは [Streamlit](https://streamlit.io/) を使って構築された Web アプリケーションで、依存関係管理には [Poetry](https://python-poetry.org/) を使用しています。Makefile を使って、インストールと実行が簡単にできるようになっています。

## 前提条件

- Python 3.7 以上

## セットアップ

1. **リポジトリをクローン**:

   ```bash
   git clone <リポジトリURL>
   cd <リポジトリディレクトリ>
   ```

2. **依存関係のインストール**:
   以下のコマンドを実行して、必要なパッケージをインストールします。

   ```bash
   make install
   ```

   これにより、requirements.txt を使って必要な依存関係がインストールされます。

## アプリケーションの実行

アプリケーションを `http://localhost:8501` で実行するには、以下のコマンドを使用します。

```bash
make run
```

これで、Streamlit サーバーがポート 8501 で起動します。デフォルトでは、CORS は無効化されています。

## Makefile コマンド

- **install**: requirements.txt を使って依存関係をインストールします。
- **run**: Streamlit アプリケーションを実行します。
