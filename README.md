# アプリ名「ぴよぴよエンジニア」

「ぴよぴよエンジニア」は、未経験からバックエンドエンジニアを目指す人向けの学習到達度診断アプリです。

■ リンク：https://piyopiyo-engineer.net/<br>
登録不要で、1分で使えるアプリです。お気軽に遊びに来てください🐣<br>
-> 2023/02 公開終了しました。

<img width="1440" alt="スクリーンショット 2023-02-05 8 04 16" src="https://user-images.githubusercontent.com/87489595/216883808-6eb966c3-f9b1-4061-86b4-fe3f58eaa360.png">

<img width="1440" alt="スクリーンショット 2023-02-05 8 04 37" src="https://user-images.githubusercontent.com/87489595/216883815-5f7ff9df-38a1-477f-a405-36739477a1bd.png">

<img width="1440" alt="スクリーンショット 2023-02-05 8 04 44" src="https://user-images.githubusercontent.com/87489595/216883821-98396507-4219-4e8d-bc03-62d796caad1a.png">

## アプリの特徴
プログラミング学習において必要な項目リストを表示し、ユーザーは学習したことのある項目にチェックを入れます。そして「診断する」のボタンを押すと、学習項目に対する進捗度がパーセンテージで表示される仕組みです。

このアプリは、私がプログラミング学習にチャレンジしたときに学習の全体像が見えず、何度も挫折してきた経験をもとにつくりました。プログラミング初心者の方や、プログラミングに少しだけ興味がある方に使ってもらえたらと考えています。

# 使用技術
## フロントエンド
- HTML
- CSS
- Bootstrap
- JavaScript

## バックエンド
- Python
- Flask
- MySQL

## インフラ
- AWS（EC2, ALB, ACM, S3, RDS, Route53, VPC, IAM）
- NGINX
- Gunicorn

## その他
- Git/GitHub
- VSCode

# 特に見ていただきたい点
- ### インフラ
  - CDパイプラインを構築している点。
  - AWSを使い、ALBを通すことで常時SSL通信を実現している点。
- ### バックエンド
  - データベースの正規化を意識してテーブル設計をしている点。
- ### フロントエンド
  - シンプルな画面遷移で、初めて使うユーザーにも操作がわかりやすい点。
- ### その他
  - チーム開発を意識し、GitHubを使った開発を実施している点。
  - 診断結果に応じて動的にツイート内容が変わる点。

## 機能一覧
- チェックリストを使った診断機能
- 診断結果のツイート機能


# 作成者
Yuriko Kikuchi（菊池百合子）

Icons made by [Chick icons created by Freepik - Flaticon](https://www.flaticon.com/free-icons/chick)
