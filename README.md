https://minnanosaiban.github.io/tomo/

# tomo

通報者本人が作成した制作物・ポートフォリオの紹介（ＰＤＦ墨消しツール・スクショＰＤＦ化ツール・サイドノート資料作成・公文書ウェブ掲載ツール・応援傍聴ナビ・Ｘスクショ管理アプリなど）と、決算/株価データ分析の連載（`blog/`）のサイト。MkDocs Material 製。

2026-09-23 に、このリポジトリは `hotline` → `kabuka` → `tomo` の順に改名した（ポートフォリオの機能も持たせるため）。ＥＮＥＯＳの内部通報制度をめぐる訴訟の内容（旧 Home・`agm/`・`trial/`）は、会社に伝えているＵＲＬを引き継いだ新しい `hotline` リポジトリ（**https://minnanosaiban.github.io/hotline/**）に移り、このリポジトリからは削除した。旧 `about/index.md` の内容が、このサイトの Home（`docs/index.md`）に昇格した。

見本帳（`docs/styleguide.md`）と、それ専用だった `docs/css/11-trial.css`・`docs/css/13-carousel.css`・`docs/js/qa-carousel.js`・`docs/js/toc-toggle.js`・`overrides/hooks/doc_indent.py` も、削除した agm/trial 専用のコンポーネントをデモしていたため合わせて削除した（`DESIGN_SYSTEM.md` にその旨の注記あり）。

## 動かし方

| 何をする | 方法 |
|---|---|
| ローカルで見る | `mkdocs_serve.bat`（`http://localhost:8000/`） |
| **公開する** | **`deploy.bat`**（ビルド → `mkdocs gh-deploy` → IndexNow → main へ push。`C:\minnanosaiban\blog` リポジトリへの push も含む） |

## 構成

- `docs/index.md` … Home（制作物の紹介、旧 about）
- `docs/blog/` … 決算/株価データ分析の連載
- `hikae/` … ローカル退避用（Git 管理せず、push しない）
