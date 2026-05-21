from __future__ import annotations

from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

from .models import WeeklyReport


def render_markdown_report(report: WeeklyReport, template_dir: Path = Path("prompts")) -> str:
    env = Environment(
        loader=FileSystemLoader(str(template_dir)),
        autoescape=select_autoescape(default=False),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    template = env.get_template("weekly_report.md.j2")
    return template.render(report=report)
