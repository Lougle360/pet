# -*- coding: utf-8 -*-
"""
规范化 MD 目录下的 Markdown：去除不必要空格、修正标点、不改变标题层级。
"""
import re
from pathlib import Path

BASE = Path(__file__).resolve().parent
MD_DIR = BASE / "MD"

# 中文标点（前不应有空格）
CP_BEFORE = "，。、；：！？」》''）】"
# 中文标点（后不应有空格，除非是换行）
CP_AFTER = "「《『（【"
# 可做破折号的「一」前后多为汉字或空格，且长度常为 1 个字符连接两段话；保守替换：仅替换明显 "某 一 某" 或 "字数字一数字" 等
DASH_PATTERN = re.compile(r"([\u4e00-\u9fff\w])\s+一\s+([\u4e00-\u9fff\w])")


def clean_line(line: str) -> str:
    # 去掉行尾空白
    s = line.rstrip("\r\n")
    # 去掉行首空白（仅当该行不是 Markdown 标题或列表时）
    if s.lstrip() and not re.match(r"^(\s*[-*+]|\s*\d+\.)\s", s) and not re.match(r"^#+\s", s):
        s = s.lstrip()
    # 标点前空格：删除紧邻在中文句号、逗号等前面的空格
    for c in CP_BEFORE:
        s = s.replace(" " + c, c)
    # 标点后多余空格
    for c in CP_AFTER:
        s = re.sub(re.escape(c) + r"\s+", c, s)
    # 错误标点
    s = s.replace("〉", "）")
    s = s.replace("〈", "（")
    # 中文引号、句号、问号前的多余空格（如 "  。" "  ？" ）
    s = re.sub(r" +([。！？】」』）])", r"\1", s)
    # Tab 或多空格连接的两段话（常为破折号误输）如 "关系\t一种" → "关系——一种"
    s = re.sub(r"([\u4e00-\u9fff])\s{2,}([一-龥])", r"\1——\2", s)
    # 连续多个空格合并为一个
    s = re.sub(r" {2,}", " ", s)
    return s


def clean_file(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    out = []
    for line in lines:
        out.append(clean_line(line))
    new_text = "\n".join(out)
    # 统一换行
    if new_text and not new_text.endswith("\n"):
        new_text += "\n"
    path.write_text(new_text, encoding="utf-8")


def main():
    for f in MD_DIR.glob("*.md"):
        clean_file(f)
        print("已处理:", f.name)


if __name__ == "__main__":
    main()
