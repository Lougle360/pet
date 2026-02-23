# -*- coding: utf-8 -*-
"""
将 DOC 目录下的 .docx 和 .epub 转为 Markdown，保存到 MD 目录。
"""
import os
import re
import sys
from pathlib import Path

# DOC 与 MD 目录（与脚本所在目录相对）
BASE = Path(__file__).resolve().parent
DOC_DIR = BASE / "DOC"
MD_DIR = BASE / "MD"


def ensure_md_dir():
    MD_DIR.mkdir(parents=True, exist_ok=True)


def style_to_level(style_name):
    """将 Word 样式名映射为 Markdown 标题级别（支持中英文样式名）。"""
    if not style_name:
        return 0
    s = style_name.lower().strip()
    # 英文：Heading 1, Title
    if "heading 1" in s or s == "title":
        return 1
    if "heading 2" in s:
        return 2
    if "heading 3" in s:
        return 3
    if "heading 4" in s:
        return 4
    if "heading 5" in s:
        return 5
    if "heading 6" in s:
        return 6
    # 中文样式名（如 标题 1、标题 2）
    if "标题 1" in style_name or "标题1" in style_name:
        return 1
    if "标题 2" in style_name or "标题2" in style_name:
        return 2
    if "标题 3" in style_name or "标题3" in style_name:
        return 3
    if "标题 4" in style_name or "标题4" in style_name:
        return 4
    if "标题 5" in style_name or "标题5" in style_name:
        return 5
    if "标题 6" in style_name or "标题6" in style_name:
        return 6
    return 0


def run_to_md(run):
    """将 docx Run 转为 Markdown 片段（加粗/斜体）。"""
    text = run.text
    if not text:
        return ""
    if run.bold and run.italic:
        return f"***{text}***"
    if run.bold:
        return f"**{text}**"
    if run.italic:
        return f"*{text}*"
    return text


def paragraph_to_md(para):
    """将 docx Paragraph 转为一行 Markdown。"""
    parts = [run_to_md(r) for r in para.runs]
    return "".join(parts)


def _iter_block_items(doc):
    """按文档顺序遍历段落与表格。"""
    from docx.document import Document as _Document
    from docx.oxml.text.paragraph import CT_P
    from docx.oxml.table import CT_Tbl
    from docx.table import Table
    from docx.text.paragraph import Paragraph

    body = doc.element.body
    for child in body.iterchildren():
        if isinstance(child, CT_P):
            yield Paragraph(child, doc)
        elif isinstance(child, CT_Tbl):
            yield Table(child, doc)


def docx_to_markdown(docx_path):
    """将单个 .docx 转为 Markdown 文本（保持段落与表格顺序）。"""
    from docx import Document
    from docx.table import Table
    from docx.text.paragraph import Paragraph

    doc = Document(docx_path)
    lines = []

    for block in _iter_block_items(doc):
        if isinstance(block, Paragraph):
            level = style_to_level(block.style.name)
            content = paragraph_to_md(block).strip()
            if level >= 1:
                lines.append("\n" + "#" * level + " " + content + "\n")
            elif content:
                # 启发式：整段为单一加粗且较短时视为二级标题（如「致父母们」「第1部分」）
                bare = content.strip("*").strip()
                if len(content) <= 50 and content.startswith("**") and content.endswith("**") and "**" not in content[2:-2] and len(bare) >= 1:
                    lines.append("\n## " + bare + "\n")
                else:
                    lines.append(content + "\n\n")
        elif isinstance(block, Table):
            rows = []
            for row in block.rows:
                cells = [cell.text.strip().replace("\n", " ") for cell in row.cells]
                rows.append("| " + " | ".join(cells) + " |")
            if rows:
                if len(rows) > 1:
                    rows.insert(1, "| " + " | ".join(["---"] * len(block.rows[0].cells)) + " |")
                lines.append("\n" + "\n".join(rows) + "\n\n")

    raw = "\n".join(lines).strip()
    return _normalize_blank_lines(raw)


def _normalize_blank_lines(text):
    """将连续 3 个及以上换行压缩为 2 个，减少多余空行。"""
    return re.sub(r"\n{3,}", "\n\n", text)


def epub_to_markdown(epub_path):
    """将 .epub 转为 Markdown 文本（提取正文 HTML 并转为纯文/简单 Markdown）。"""
    import ebooklib
    from ebooklib import epub
    from bs4 import BeautifulSoup

    try:
        book = epub.read_epub(epub_path)
    except Exception as e:
        return f"<!-- 读取 EPUB 失败: {e} -->\n"

    parts = []
    for item in book.get_items():
        if item.get_type() != ebooklib.ITEM_DOCUMENT:
            continue
        html = item.get_content().decode("utf-8", errors="replace")
        soup = BeautifulSoup(html, "html.parser")
        body = soup.find("body")
        if not body:
            continue
        part = _html_body_to_md(body)
        if part.strip():
            parts.append(part)
    raw = "\n\n".join(parts).strip()
    return _normalize_blank_lines(raw)


def _html_body_to_md(body):
    """将 HTML body 转为简单 Markdown（标题 + 段落）。"""
    lines = []
    for el in body.find_all(["h1", "h2", "h3", "h4", "h5", "h6", "p", "li", "div"]):
        text = el.get_text(separator=" ", strip=True)
        if not text:
            continue
        if el.name == "h1":
            lines.append("\n# " + text + "\n")
        elif el.name == "h2":
            lines.append("\n## " + text + "\n")
        elif el.name == "h3":
            lines.append("\n### " + text + "\n")
        elif el.name == "h4":
            lines.append("\n#### " + text + "\n")
        elif el.name == "h5":
            lines.append("\n##### " + text + "\n")
        elif el.name == "h6":
            lines.append("\n###### " + text + "\n")
        elif el.name == "li":
            lines.append("- " + text + "\n")
        else:
            lines.append(text + "\n\n")
    return "\n".join(lines)


def main():
    ensure_md_dir()
    converted = []
    errors = []

    for path in sorted(DOC_DIR.iterdir()):
        if not path.is_file():
            continue
        name = path.name
        stem = path.stem
        out_name = stem + ".md"
        out_path = MD_DIR / out_name

        try:
            if name.lower().endswith(".docx"):
                md_text = docx_to_markdown(path)
                out_path.write_text(md_text, encoding="utf-8")
                converted.append(name)
            elif name.lower().endswith(".epub"):
                md_text = epub_to_markdown(path)
                out_path.write_text(md_text, encoding="utf-8")
                converted.append(name)
            else:
                continue
        except Exception as e:
            errors.append((name, str(e)))

    for f in converted:
        print("已转换:", f)
    for f, err in errors:
        print("失败:", f, "—", err, file=sys.stderr)

    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
