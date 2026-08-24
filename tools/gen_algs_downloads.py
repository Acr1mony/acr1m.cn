#!/usr/bin/env python3
"""Generate downloadable .md / .docx for the ALGS Interactive Replay post."""
from __future__ import annotations

import re
import zipfile
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "source" / "_posts" / "ALGS Interactive Replay功能介绍.md"
OUT_DIR = ROOT / "source" / "downloads"
MD_OUT = OUT_DIR / "algs-interactive-replay.md"
DOCX_OUT = OUT_DIR / "algs-interactive-replay.docx"


def strip_front_matter(text: str) -> str:
    if not text.startswith("---"):
        return text
    parts = text.split("---", 2)
    if len(parts) >= 3:
        return parts[2].lstrip("\n")
    return text


def runs_from_inline(s: str) -> list[dict]:
    token_re = re.compile(
        r"\*\*(.+?)\*\*|`([^`]+)`|\[([^\]]+)\]\(([^)]+)\)|(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)"
    )
    runs: list[dict] = []
    pos = 0
    for m in token_re.finditer(s):
        if m.start() > pos:
            runs.append({"t": s[pos : m.start()]})
        if m.group(1) is not None:
            runs.append({"t": m.group(1), "bold": True})
        elif m.group(2) is not None:
            runs.append({"t": m.group(2), "code": True})
        elif m.group(3) is not None:
            runs.append({"t": m.group(3), "link": m.group(4)})
        elif m.group(5) is not None:
            runs.append({"t": m.group(5), "italic": True})
        pos = m.end()
    if pos < len(s):
        runs.append({"t": s[pos:]})
    if not runs:
        runs = [{"t": s}]
    return runs


def run_xml(run: dict) -> str:
    t = escape(run.get("t", ""))
    rpr: list[str] = []
    if run.get("bold"):
        rpr.append("<w:b/>")
    if run.get("italic"):
        rpr.append("<w:i/>")
    if run.get("code"):
        rpr.append('<w:rFonts w:ascii="Consolas" w:hAnsi="Consolas"/>')
        rpr.append('<w:sz w:val="20"/>')
    rpr_xml = f"<w:rPr>{''.join(rpr)}</w:rPr>" if rpr else ""
    if run.get("link"):
        url = escape(run["link"])
        return (
            f"<w:r>{rpr_xml}<w:t xml:space=\"preserve\">{t}</w:t></w:r>"
            f'<w:r><w:t xml:space="preserve"> (</w:t></w:r>'
            f'<w:r><w:rPr><w:color w:val="0563C1"/><w:u w:val="single"/></w:rPr>'
            f'<w:t xml:space="preserve">{url}</w:t></w:r>'
            f"<w:r><w:t>)</w:t></w:r>"
        )
    return f'<w:r>{rpr_xml}<w:t xml:space="preserve">{t}</w:t></w:r>'


def p_xml(text: str, style: str | None = None, bullet: bool = False) -> str:
    runs_xml = "".join(run_xml(r) for r in runs_from_inline(text))
    if style:
        ppr = f'<w:pPr><w:pStyle w:val="{style}"/></w:pPr>'
    elif bullet:
        ppr = (
            '<w:pPr><w:pStyle w:val="ListParagraph"/>'
            '<w:numPr><w:ilvl w:val="0"/><w:numId w:val="1"/></w:numPr></w:pPr>'
        )
    else:
        ppr = ""
    return f"<w:p>{ppr}{runs_xml}</w:p>"


def table_xml(rows: list[list[str]]) -> str:
    cols = max((len(r) for r in rows), default=0)
    width = 9000 // max(cols, 1)
    grid = "".join(f'<w:gridCol w:w="{width}"/>' for _ in range(cols))
    trs: list[str] = []
    for ri, row in enumerate(rows):
        tcs: list[str] = []
        for ci in range(cols):
            cell = row[ci].strip() if ci < len(row) else ""
            shading = (
                '<w:shd w:val="clear" w:color="auto" w:fill="E7E6E6"/>' if ri == 0 else ""
            )
            tcs.append(
                f'<w:tc><w:tcPr><w:tcW w:w="{width}" w:type="dxa"/>{shading}</w:tcPr>'
                f"{p_xml(cell)}</w:tc>"
            )
        trs.append(f"<w:tr>{''.join(tcs)}</w:tr>")
    borders = (
        '<w:tblBorders>'
        '<w:top w:val="single" w:sz="4" w:space="0" w:color="999999"/>'
        '<w:left w:val="single" w:sz="4" w:space="0" w:color="999999"/>'
        '<w:bottom w:val="single" w:sz="4" w:space="0" w:color="999999"/>'
        '<w:right w:val="single" w:sz="4" w:space="0" w:color="999999"/>'
        '<w:insideH w:val="single" w:sz="4" w:space="0" w:color="999999"/>'
        '<w:insideV w:val="single" w:sz="4" w:space="0" w:color="999999"/>'
        "</w:tblBorders>"
    )
    return (
        f'<w:tbl><w:tblPr><w:tblW w:w="9000" w:type="dxa"/>{borders}</w:tblPr>'
        f"<w:tblGrid>{grid}</w:tblGrid>{''.join(trs)}</w:tbl>"
    )


def md_to_paragraphs(body: str) -> list[str]:
    paras: list[str] = []
    lines = body.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]

        if "|" in line and line.strip().startswith("|"):
            rows: list[list[str]] = []
            while i < len(lines) and "|" in lines[i] and lines[i].strip().startswith("|"):
                raw = lines[i].strip().strip("|")
                cells = [c.strip() for c in raw.split("|")]
                if all(
                    re.fullmatch(r":?-+:?", c.replace(" ", "")) for c in cells if c != ""
                ):
                    i += 1
                    continue
                rows.append(cells)
                i += 1
            if rows:
                paras.append(table_xml(rows))
                paras.append("<w:p/>")
            continue

        if line.startswith("# "):
            paras.append(p_xml(line[2:].strip(), "Heading1"))
        elif line.startswith("## "):
            paras.append(p_xml(line[3:].strip(), "Heading2"))
        elif line.startswith("### "):
            paras.append(p_xml(line[4:].strip(), "Heading3"))
        elif line.strip() == "---":
            paras.append(
                '<w:p><w:pPr><w:pBdr>'
                '<w:bottom w:val="single" w:sz="6" w:space="1" w:color="CCCCCC"/>'
                "</w:pBdr></w:pPr></w:p>"
            )
        elif line.startswith("> "):
            chunks = [line[2:]]
            i += 1
            while i < len(lines) and lines[i].startswith("> "):
                chunks.append(lines[i][2:])
                i += 1
            text = " ".join(c.strip() for c in chunks)
            runs_xml = "".join(run_xml(r) for r in runs_from_inline(text))
            paras.append(
                "<w:p><w:pPr><w:ind w:left=\"420\"/><w:pBdr>"
                '<w:left w:val="single" w:sz="18" w:space="8" w:color="999999"/>'
                f"</w:pBdr></w:pPr>{runs_xml}</w:p>"
            )
            continue
        elif re.match(r"^[-*] ", line):
            paras.append(p_xml(line[2:].strip(), bullet=True))
        elif re.match(r"^\d+\. ", line):
            paras.append(p_xml(line.strip()))
        elif line.strip() == "":
            pass
        else:
            paras.append(p_xml(line.strip()))
        i += 1
    return paras


CONTENT_TYPES = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
  <Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
  <Override PartName="/word/numbering.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.numbering+xml"/>
</Types>
"""

RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>
"""

DOC_RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/numbering" Target="numbering.xml"/>
</Relationships>
"""

STYLES = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:style w:type="paragraph" w:default="1" w:styleId="Normal">
    <w:name w:val="Normal"/>
    <w:qFormat/>
    <w:rPr>
      <w:rFonts w:ascii="Microsoft YaHei" w:hAnsi="Microsoft YaHei" w:eastAsia="Microsoft YaHei"/>
      <w:sz w:val="22"/>
      <w:szCs w:val="22"/>
    </w:rPr>
  </w:style>
  <w:style w:type="paragraph" w:styleId="Heading1">
    <w:name w:val="heading 1"/>
    <w:basedOn w:val="Normal"/>
    <w:next w:val="Normal"/>
    <w:qFormat/>
    <w:pPr><w:spacing w:before="360" w:after="200"/><w:outlineLvl w:val="0"/></w:pPr>
    <w:rPr><w:b/><w:sz w:val="36"/><w:szCs w:val="36"/></w:rPr>
  </w:style>
  <w:style w:type="paragraph" w:styleId="Heading2">
    <w:name w:val="heading 2"/>
    <w:basedOn w:val="Normal"/>
    <w:next w:val="Normal"/>
    <w:qFormat/>
    <w:pPr><w:spacing w:before="280" w:after="160"/><w:outlineLvl w:val="1"/></w:pPr>
    <w:rPr><w:b/><w:sz w:val="28"/><w:szCs w:val="28"/></w:rPr>
  </w:style>
  <w:style w:type="paragraph" w:styleId="Heading3">
    <w:name w:val="heading 3"/>
    <w:basedOn w:val="Normal"/>
    <w:next w:val="Normal"/>
    <w:qFormat/>
    <w:pPr><w:spacing w:before="240" w:after="120"/><w:outlineLvl w:val="2"/></w:pPr>
    <w:rPr><w:b/><w:sz w:val="24"/><w:szCs w:val="24"/></w:rPr>
  </w:style>
  <w:style w:type="paragraph" w:styleId="ListParagraph">
    <w:name w:val="List Paragraph"/>
    <w:basedOn w:val="Normal"/>
    <w:qFormat/>
    <w:pPr><w:ind w:left="720"/></w:pPr>
  </w:style>
</w:styles>
"""

NUMBERING = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:numbering xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:abstractNum w:abstractNumId="0">
    <w:multiLevelType w:val="hybridMultilevel"/>
    <w:lvl w:ilvl="0">
      <w:start w:val="1"/>
      <w:numFmt w:val="bullet"/>
      <w:lvlText w:val="•"/>
      <w:lvlJc w:val="left"/>
      <w:pPr><w:ind w:left="720" w:hanging="360"/></w:pPr>
    </w:lvl>
  </w:abstractNum>
  <w:num w:numId="1">
    <w:abstractNumId w:val="0"/>
  </w:num>
</w:numbering>
"""


def write_docx(body: str, path: Path) -> None:
    paras = md_to_paragraphs(body)
    document_xml = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"
 xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
  <w:body>
    {''.join(paras)}
    <w:sectPr>
      <w:pgSz w:w="11906" w:h="16838"/>
      <w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440"/>
    </w:sectPr>
  </w:body>
</w:document>
"""
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", CONTENT_TYPES)
        z.writestr("_rels/.rels", RELS)
        z.writestr("word/document.xml", document_xml)
        z.writestr("word/_rels/document.xml.rels", DOC_RELS)
        z.writestr("word/styles.xml", STYLES)
        z.writestr("word/numbering.xml", NUMBERING)


def main() -> None:
    text = SRC.read_text(encoding="utf-8")
    body = strip_front_matter(text)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    MD_OUT.write_text(body, encoding="utf-8")
    write_docx(body, DOCX_OUT)
    print(f"wrote {MD_OUT.relative_to(ROOT)} ({MD_OUT.stat().st_size} bytes)")
    print(f"wrote {DOCX_OUT.relative_to(ROOT)} ({DOCX_OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
