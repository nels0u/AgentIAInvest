from __future__ import annotations

from datetime import date, timedelta
from pathlib import Path

from .config import load_settings
from .models import AssetSnapshot, GeopoliticalEvent, MacroIndicator, WeeklyReport
from .reporting import render_markdown_report


def _build_placeholder_report() -> WeeklyReport:
    today = date.today()
    start = today - timedelta(days=7)

    return WeeklyReport(
        period_start=start,
        period_end=today,
        generated_at=today,
        key_takeaway=(
            "Le momentum actions reste positif, mais la hausse des taux longs et "
            "les tensions géopolitiques augmentent le risque de volatilité à court terme."
        ),
        market_moves=[
            AssetSnapshot(symbol="SPY", name="S&P 500 ETF", category="etf", period_return_pct=1.2),
            AssetSnapshot(symbol="QQQ", name="Nasdaq 100 ETF", category="etf", period_return_pct=2.0),
            AssetSnapshot(symbol="TLT", name="US 20Y Treasury", category="etf", period_return_pct=-0.8),
        ],
        macro_updates=[
            MacroIndicator(name="US CPI YoY", value=3.1, unit="%", previous_value=3.0, release_date=today),
            MacroIndicator(name="US Unemployment", value=4.0, unit="%", previous_value=3.9, release_date=today),
        ],
        geopolitical_updates=[
            GeopoliticalEvent(
                title="Nouvelles tensions sur une route énergétique stratégique",
                source="Reuters",
                region="Middle East",
                date=today,
                impact_level="high",
                summary="Hausse du prix du pétrole et pression inflationniste potentielle.",
            )
        ],
        risks=[
            "Persistante inflation des services pouvant retarder les baisses de taux.",
            "Risque d'escalade géopolitique sur l'énergie.",
        ],
        opportunities=[
            "Qualité défensive avec croissance bénéficiaire résiliente.",
            "Entrées progressives sur ETF larges en cas de correction technique.",
        ],
    )


def run() -> Path:
    settings = load_settings()
    report = _build_placeholder_report()
    content = render_markdown_report(report)

    output_dir = Path("output")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / f"weekly_report_{report.period_end.isoformat()}.md"
    output_file.write_text(content, encoding="utf-8")

    print(f"Report generated: {output_file} | source_count={len(settings.sources)}")
    return output_file


if __name__ == "__main__":
    run()
