# blog.h4y4bus4.com

## これは何
- blog.h4y4bus4.com にホストされるコンテンツのリポジトリです。

## 備忘: 手元でのライブプレビュー
```
## localhost:8080 
$ docker run -u "$(id -u):$(id -g)" -v $PWD:/app --workdir /app -p 8080:8080 ghcr.io/getzola/zola:v0.19.1 serve --interface 0.0.0.0 --port 8080 --base-url localhost
```

## 備忘: ビルドとデプロイ
```
$ git add .
$ git commit -m "commmmit"
$ git push
```
https://dash.cloudflare.com でデプロイの様子を見守る。

## ライセンス/License
このリポジトリのコンテンツは GPL-3.0 に基づいて公開されます。

The content of this repository is available under the terms of the GPL-3.0.