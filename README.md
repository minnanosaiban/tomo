# tomo

**https://minnanosaiban.github.io/tomo/**

通報者本人が作った制作物の紹介（ポートフォリオ）のサイトです。MkDocs Material 製で、GitHub Pages で公開しています。

## 載せているもの

| 場所 | 中身 |
|---|---|
| Home（`docs/index.md`） | 制作物の一覧と運営者について |
| 技術解説（`docs/tech/`） | 各制作物の仕組みと、作るうえで判断したことの解説 |
| 決算・株価データ検証 | 2026-10-11 に別サイト [kessan-kabuka](https://minnanosaiban.github.io/kessan-kabuka/) へ分離（`docs/blog/` には旧URLからの転送ページだけを残している） |

### 技術解説の一覧

| 制作物 | 解説 |
|---|---|
| ＰＤＦツール | [`pdf-tools.md`](docs/tech/pdf-tools.md) |
| サイドノート作成 | [`sidenote.md`](docs/tech/sidenote.md) |
| RelaGrid　関係図 | [`relagrid.md`](docs/tech/relagrid.md) |
| スキャン墨消し | [`scan-ocr.md`](docs/tech/scan-ocr.md) |
| スクショＰＤＦ化 | [`screenshot-pdf.md`](docs/tech/screenshot-pdf.md) |
| Ｘスクショ管理ツール | [`screenshot-x.md`](docs/tech/screenshot-x.md)（準備中） |
| 応援傍聴ナビ | [`court-calendar.md`](docs/tech/court-calendar.md) |
| 内部通報制度をめぐる裁判記録 | [`hotline.md`](docs/tech/hotline.md) |
| ウェブサイトデザイン | [`web-design.md`](docs/tech/web-design.md) |
| 有報ナビ | [`stock-analysis.md`](docs/tech/stock-analysis.md) |
| E資格 動く数式ノート | [`e-shikaku.md`](docs/tech/e-shikaku.md) |

解説の図は、[RelaGrid](https://minnanosaiban.github.io/relagrid/) で描いたものが多くあります。図の元になった記述（DSL）は、RelaGrid リポジトリの `examples/` にあります（`docs/img/` の SVG と対応）。

## 動かし方

| 何をする | 方法 |
|---|---|
| ローカルで見る | `mkdocs_serve.bat`（`http://localhost:8000/`） |
| **公開する** | **`deploy.bat`**（ビルド → `mkdocs gh-deploy` → IndexNow → main へ push。`C:\minnanosaiban\blog` リポジトリへの push も含む） |

依存は `requirements.txt` にあります。

## 数式を書くとき

ページの先頭（front matter）に `math: true` と書いたページだけ、数式（KaTeX）が使えます。書かないページは、これまでと同じ HTML のままで、KaTeX は読み込みません。

```yaml
---
title: ページ名
math: true
---
```

本文では、行内は `$...$`、ブロックは `$$...$$`（前後に空行）で書きます。仕組みは、`mkdocs.yml` の `pymdownx.arithmatex`（目印を HTML にする）、`overrides/main.html`（`math: true` のページだけ KaTeX を読み込む）、`docs/js/katex-init.js`（描画）の3つです。

## 構成

```
docs/
  index.md        Home
  tech/           技術解説
  blog/           旧URLからの転送ページ（決算・株価データ検証は kessan-kabuka へ移転）
  img/            図（SVG）・カード画像
  css/shared/     共通デザイン（minna-design から同期。直接編集しない）
  css/ js/        スタイルとスクリプト
overrides/        MkDocs Material のテンプレート上書き・フック
scripts/          IndexNow への通知
hikae/            ローカル退避用（Git 管理せず、push しない）
DESIGN_SYSTEM.md  hotline 時代のコンポーネント棚卸し（履歴）。現行の共通デザインは minna-design
```

## 経緯

- 2026-09-23 に、このリポジトリは `hotline` → `kabuka` → `tomo` の順に改名しました（ポートフォリオの機能も持たせるため）
- ＥＮＥＯＳの内部通報制度をめぐる訴訟の内容（旧 Home・`agm/`・`trial/`）は、会社に伝えているＵＲＬを引き継いだ新しい `hotline` リポジトリ（**https://minnanosaiban.github.io/hotline/**）に移り、このリポジトリからは削除しました。旧 `about/index.md` の内容が、このサイトの Home に昇格しました
- 削除した agm/trial 専用のコンポーネントをデモしていた見本帳（`docs/styleguide.md`）と、専用の `docs/css/11-trial.css`・`docs/css/13-carousel.css`・`docs/js/qa-carousel.js`・`docs/js/toc-toggle.js`・`overrides/hooks/doc_indent.py` も合わせて削除しました（`DESIGN_SYSTEM.md` に注記があります）
- 2026-10-11 に、決算・株価データ検証を別リポジトリ [kessan-kabuka](https://github.com/minnanosaiban/kessan-kabuka)（Zensical 製）へ分離しました。共通デザインは [minna-design](https://github.com/minnanosaiban/minna-design) に切り出し、tomo・hotline・kessan-kabuka で共有します（同期は minna-design の `sync.bat`）
