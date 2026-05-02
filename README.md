# blog.2haya.net

## これは何
- blog.2haya.net にホストされるコンテンツのリポジトリです。

## 環境構築
このリポジトリをクローンしたのち、以下のように submodule を初期化する。

```
$ git submodule init
$ git submodule update --init
```

## コンテンツの追加
blog への追加の場合
```
$ new-blog-post.sh <title>
```

article への追加の場合
```
$ new-article-post.sh <title>
```

**注意**
画像添付時は以下のように exif 情報を削除しておくこと。
```
$ exiftool -all= *.jpg
```

## 手元でのライブプレビュー
```
## localhost:8080
$ docker run -u "$(id -u):$(id -g)" -v $PWD:/app --workdir /app -p 8080:8080 ghcr.io/getzola/zola:v0.19.1 serve --interface 0.0.0.0 --port 8080 --base-url localhost
```

## ビルドとデプロイ
```
$ git add .
$ git commit -m "commmmit"
$ git push
```
https://dash.cloudflare.com でデプロイの様子を見守る。

## ライセンス/License
このリポジトリのコンテンツは GPL-3.0 に基づいて公開されます。

The content of this repository is available under the terms of the GPL-3.0.
