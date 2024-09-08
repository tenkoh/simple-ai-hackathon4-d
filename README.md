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

3. **API キーの設定**:
   このプロジェクトでは、[OpenAI](https://platform.openai.com/) の API キーが必要です。API キーを取得して、`.env` ファイルに設定してください。

   ```bash
   cp .env.example .env
   ```

   `.env` ファイルを開いて、`OPENAI_API_KEY` の値を設定してください。

   ```bash
   OPENAI_API_KEY=<APIキー>
   ```

   これで、API キーが設定されました。

## アプリケーションの実行

アプリケーションを `http://localhost:8501` で実行するには、以下のコマンドを使用します。

```bash
make run
```

これで、Streamlit サーバーがポート 8501 で起動します。デフォルトでは、CORS は無効化されています。

## Makefile コマンド

- **install**: requirements.txt を使って依存関係をインストールします。
- **run**: Streamlit アプリケーションを実行します。

## Cloud Run へのデプロイ

以下の手順で Cloud Run へデプロイできます

- デプロイ先のプロジェクトへログインします

```sh
gcloud auth login
gcloud config set project <your-project-id>
```

- 利用するサービスを有効化します

```sh
gcloud services enable compute.googleapis.com run.googleapis.com \
    artifactregistry.googleapis.com cloudbuild.googleapis.com
```

有効化されるサービスは以下のとおりです。

`compute.googleapis.com` ▶︎ Compute Engine、仮想マシンが利用できます。
`run.googleapis.com` ▶︎ Cloud Run、コンテナアプリをホスト。
`artifactregistry.googleapis.com` ▶︎ Artifact Registry、Docker イメージ の保存。
`cloudbuild.googleapis.com` ▶︎ Cloud Build、サーバーレスな CI 環境です。

- 以下のコマンドを実行すると Cloud Run へデプロイされます

```sh
gcloud run deploy my-app --region "asia-northeast1" --source . \
    --allow-unauthenticated --quiet --update-env-vars OPENAI_API_KEY=<OPENAI_API_KEY>
```
