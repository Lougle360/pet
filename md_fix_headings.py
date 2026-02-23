# -*- coding: utf-8 -*-
"""
修正 MD 标题层级：章为 H2(##)，节为 H3(###)，小节为 H4(####)。
"""
import re
from pathlib import Path

BASE = Path(__file__).resolve().parent
MD_DIR = BASE / "MD"

# 保持为 ## 的标题（书级/前言）
KEEP_H2 = {"我的人际关系信条", "致父母们", "家庭学习建议", "目录"}


def fix_parent_effectiveness(path: Path) -> None:
    """父母效能训练.md：第N章为 ##，其余正文节标题为 ###。"""
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    out = []
    for line in lines:
        s = line
        # 将 **第N章** **XXX** 规范为 ## 第N章 XXX
        m = re.match(r"^\*\*第(\d+)章\*\*\s*\**(.*?)\**\s*$", s)
        if m:
            s = "## 第{}章 {}".format(m.group(1), m.group(2).strip()).rstrip()
            out.append(s)
            continue
        # 已是 ## 第N章 的保持
        if re.match(r"^## 第\d+章\s", s):
            out.append(s)
            continue
        # 需要保持为 H2 的
        for t in KEEP_H2:
            if s.strip() == "## " + t or s == "## " + t:
                out.append(s)
                break
        else:
            # 其他 ## 标题改为 ###（节）
            if s.startswith("## ") and not s.startswith("### "):
                s = "### " + s[3:]
            out.append(s)
    path.write_text("\n".join(out) + "\n", encoding="utf-8")


def fix_30years(path: Path) -> None:
    """30周年纪念版：第N章保持 ##，其余 ## 改为 ###。"""
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    out = []
    for line in lines:
        s = line
        # **第 N 章** **标题** → ## 第N章 标题
        m = re.match(r"^\*\*第\s*(\d+)\s*章\*\*\s*\**(.*?)\**", s)
        if m:
            title = re.sub(r"\s+", " ", m.group(2).strip()).strip()
            s = "## 第{}章 {}".format(m.group(1), title)
            out.append(s)
            continue
        if re.match(r"^## 第\d+章\s", s):
            out.append(s)
            continue
        # 非「第N章」的 ## 改为 ###
        if s.startswith("## ") and not s.startswith("### "):
            s = "### " + s[3:]
        out.append(s)
    path.write_text("\n".join(out) + "\n", encoding="utf-8")


def main():
    for name in ["父母效能训练.md", "父母效能训练手册 30周年纪念版 戈登.md"]:
        path = MD_DIR / name
        if not path.exists():
            continue
        if "30周年" in name:
            fix_30years(path)
        else:
            fix_parent_effectiveness(path)
        print("已处理:", name)


if __name__ == "__main__":
    main()
