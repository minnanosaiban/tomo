# -*- coding: utf-8 -*-
import re

def on_post_page(output, page, **kwargs):
    src = page.file.src_path.replace("\\", "/")
    if src.startswith("blog/posts/"):
        # 個別記事：共通の blog-post-page に加え、記事専用クラスも付与（一覧と区別するため）
        output = re.sub(r"(<body\b)", r'\1 class="blog-post-page blog-article-page"', output, count=1)
    elif src == "blog/glossary.md":
        # 用語集：記事と同じ読み物スタイルを当てる
        output = re.sub(r"(<body\b)", r'\1 class="blog-post-page blog-article-page"', output, count=1)
    elif src == "blog/index.md":
        output = re.sub(r"(<body\b)", r'\1 class="blog-post-page"', output, count=1)
    return output
