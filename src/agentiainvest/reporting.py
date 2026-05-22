from __future__ import annotations

from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

from .models import WeeklyReport


def _build_env(template_dir: Path) -> Environment:
    return Environment(
        loader=FileSystemLoader(str(template_dir)),
        autoescape=select_autoescape(default=True, enabled_extensions=("html", "xml")),
        trim_blocks=True,
        lstrip_blocks=True,
    )


def render_html_report(report: WeeklyReport, template_dir: Path = Path("prompts")) -> str:
    env = _build_env(template_dir)
    template = env.get_template("weekly_report.html.j2")
    return template.render(report=report)
