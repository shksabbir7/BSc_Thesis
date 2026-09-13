"""Render the Chapter 6 Bangla example table as a high-contrast PNG."""

from src.common.seed import set_seed

set_seed()

import html
import json
import os
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RESULT = ROOT / "results" / "s5_error_examples_bn_v1.json"
OUT_DIRS = (ROOT / "docs" / "chapters" / "chapter6" / "figures",)

ROLES = {
    "E1": "Baseline failure (L0)",
    "E2": "Baseline failure (L1)",
    "E3": "Residual failure (L0)",
    "E4": "Residual failure (L1)",
    "E5": "Repaired output (L0)",
    "E6": "Budget exhaustion (L1)",
}


def wrap_words(text: str, limit: int = 38) -> list[str]:
    lines: list[str] = []
    line = ""
    for word in text.split():
        candidate = f"{line} {word}".strip()
        if line and len(candidate) > limit:
            lines.append(line)
            line = word
        else:
            line = candidate
    if line:
        lines.append(line)
    return lines


def build_svg() -> str:
    payload = json.loads(RESULT.read_text(encoding="utf-8"))
    source = payload["result"]["examples"]
    texts = {item["id"]: item["selected"]["text"] for item in source}
    rows = [
        (key, ROLES[key], wrap_words(texts[key], 50 if key == "E1" else 38))
        for key in ROLES
    ]

    width = 1400
    left, right = 36, 1364
    x_id, x_role, x_text = 58, 205, 535
    header_y = 96
    heights = [max(96, 36 + len(lines) * 45) for _, _, lines in rows]
    height = 142 + sum(heights) + 38

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        "<style>",
        "text{fill:#000;text-rendering:geometricPrecision}",
        ".head{font-family:'Times New Roman',serif;font-size:32px;font-weight:700}",
        ".meta{font-family:'Times New Roman',serif;font-size:29px;font-weight:500}",
        ".bn{font-family:'Nirmala UI','SolaimanLipi',sans-serif;font-size:32px;font-weight:500}",
        ".rule{stroke:#111;stroke-width:2.8;shape-rendering:crispEdges}",
        ".light{stroke:#555;stroke-width:1.5;shape-rendering:crispEdges}",
        "</style>",
        '<rect width="100%" height="100%" fill="#fff"/>',
        f'<line x1="{left}" y1="36" x2="{right}" y2="36" class="rule"/>',
        f'<text x="{x_id}" y="{header_y}" class="head">Example</text>',
        f'<text x="{x_role}" y="{header_y}" class="head">Selection role</text>',
        f'<text x="{x_text}" y="{header_y}" class="head">Generated Bangla response</text>',
        f'<line x1="{left}" y1="124" x2="{right}" y2="124" class="rule"/>',
    ]

    y = 124
    for index, (example_id, role, lines) in enumerate(rows):
        row_height = heights[index]
        centre = y + row_height / 2
        parts.append(f'<text x="{x_id}" y="{centre + 10}" class="meta">{example_id}</text>')
        parts.append(f'<text x="{x_role}" y="{centre + 10}" class="meta">{html.escape(role)}</text>')
        first_y = centre - (len(lines) - 1) * 22.5 + 11
        for line_index, line in enumerate(lines):
            parts.append(
                f'<text x="{x_text}" y="{first_y + line_index * 45}" class="bn">'
                f"{html.escape(line)}</text>"
            )
        y += row_height
        rule_class = "rule" if index == len(rows) - 1 else "light"
        parts.append(f'<line x1="{left}" y1="{y}" x2="{right}" y2="{y}" class="{rule_class}"/>')
    parts.append("</svg>")
    return "".join(parts)


def render_png(svg_path: Path, png_path: Path) -> None:
    script = (
        "const sharp=require('sharp');"
        "sharp(process.argv[1],{density:320}).png({compressionLevel:9})"
        ".toFile(process.argv[2]).then(x=>console.log(`${x.width}x${x.height}`));"
    )
    environment = os.environ.copy()
    bundled_modules = Path(
        r"C:\Users\acer\.cache\codex-runtimes\codex-primary-runtime\dependencies\node\node_modules"
    )
    if bundled_modules.exists():
        environment["NODE_PATH"] = str(bundled_modules)
    subprocess.run(
        ["node", "-e", script, str(svg_path), str(png_path)],
        cwd=ROOT,
        env=environment,
        check=True,
    )


def main() -> None:
    svg = build_svg()
    for output_dir in OUT_DIRS:
        output_dir.mkdir(parents=True, exist_ok=True)
        svg_path = output_dir / "bangla_error_examples_table.svg"
        png_path = output_dir / "bangla_error_examples_table.png"
        svg_path.write_text(svg, encoding="utf-8", newline="\n")
        render_png(svg_path, png_path)
        print(png_path.relative_to(ROOT))


if __name__ == "__main__":
    main()
