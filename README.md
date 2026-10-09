# tomo

**https://minnanosaiban.github.io/tomo/**

通報者本人が作った制作物の紹介（ポートフォリオ）と、決算・株価データの検証を載せたサイトです。MkDocs Material 製で、GitHub Pages で公開しています。

## 載せているもの

| 場所 | 中身 |
|---|---|
| Home（`docs/index.md`） | 制作物の一覧と運営者について |
| 技術解説（`docs/tech/`） | 各制作物の仕組みと、作るうえで判断したことの解説 |
| 株価分析（`docs/blog/`） | 決算・株価データの検証 |

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
| ＥＮＥＯＳの内部通報制度をめぐる訴訟について | [`hotline.md`](docs/tech/hotline.md) |
| 有報ナビ | [`stock-analysis.md`](docs/tech/stock-analysis.md) |

解説の図は、[RelaGrid](https://minnanosaiban.github.io/relagrid/) で描いたものが多くあります。図の元になった記述（DSL）は、RelaGrid リポジトリの `examples/` にあります（`docs/img/` の SVG と対応）。

## 動かし方

| 何をする | 方法 |
|---|---|
| ローカルで見る | `mkdocs_serve.bat`（`http://localhost:8000/`） |
| **公開する** | **`deploy.bat`**（ビルド → `mkdocs gh-deploy` → IndexNow → main へ push。`C:\minnanosaiban\blog` リポジトリへの push も含む） |

依存は `requirements.txt` にあります。

## 構成

```
docs/
  index.md        Home
  tech/           技術解説
  blog/           決算・株価データの検証
  img/            図（SVG）・カード画像
  css/ js/        スタイルとスクリプト
overrides/        MkDocs Material のテンプレート上書き・フック
scripts/          IndexNow への通知
hikae/            ローカル退避用（Git 管理せず、push しない）
DESIGN_SYSTEM.md  このサイトのデザインシステム
```

## 経緯

- 2026-09-23 に、このリポジトリは `hotline` → `kabuka` → `tomo` の順に改名しました（ポートフォリオの機能も持たせるため）
- ＥＮＥＯＳの内部通報制度をめぐる訴訟の内容（旧 Home・`agm/`・`trial/`）は、会社に伝えているＵＲＬを引き継いだ新しい `hotline` リポジトリ（**https://minnanosaiban.github.io/hotline/**）に移り、このリポジトリからは削除しました。旧 `about/index.md` の内容が、このサイトの Home に昇格しました
- 削除した agm/trial 専用のコンポーネントをデモしていた見本帳（`docs/styleguide.md`）と、専用の `docs/css/11-trial.css`・`docs/css/13-carousel.css`・`docs/js/qa-carousel.js`・`docs/js/toc-toggle.js`・`overrides/hooks/doc_indent.py` も合わせて削除しました（`DESIGN_SYSTEM.md` に注記があります）
