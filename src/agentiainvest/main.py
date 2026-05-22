from __future__ import annotations

from datetime import date, timedelta
from pathlib import Path

from .config import load_settings
from .models import AssetSnapshot, GeopoliticalEvent, MacroIndicator, WeeklyReport
from .reporting import render_html_report


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
            AssetSnapshot(symbol="SPY", name="S&P 500", category="index", period_return_pct=1.5),
            AssetSnapshot(symbol="NDX", name="NASDAQ 100", category="index", period_return_pct=2.6),
            AssetSnapshot(symbol="SX5E", name="Stoxx 600", category="index", period_return_pct=0.8),
            AssetSnapshot(symbol="NKY", name="Nikkei 225", category="index", period_return_pct=-0.6),
            AssetSnapshot(symbol="EEM", name="MSCI Emerging Markets", category="etf", period_return_pct=0.4),
            AssetSnapshot(symbol="BZ=F", name="Brent Pétrole", category="commodity", period_return_pct=3.8),
            AssetSnapshot(symbol="GLD", name="Or (USD/oz)", category="commodity", period_return_pct=0.9),
            AssetSnapshot(symbol="US10Y", name="US 10Y (Taux)", category="bond", period_return_pct=0.04),
        ],
        remarkable_moves=[
            AssetSnapshot(symbol="IXN", name="MSCI World IT (Tech)", category="etf", period_return_pct=3.2),
            AssetSnapshot(symbol="HACK", name="ETF Cybersécurité", category="etf", period_return_pct=4.7),
            AssetSnapshot(symbol="LUX", name="Indices Luxury Brands", category="equity", period_return_pct=-1.2),
            AssetSnapshot(symbol="SOXX", name="ETF Semi-conducteurs", category="etf", period_return_pct=4.3),
            AssetSnapshot(symbol="ICLN", name="ETF Énergie propre", category="etf", period_return_pct=1.6),
            AssetSnapshot(symbol="IXG", name="ETF Banques globales", category="etf", period_return_pct=1.3),
            AssetSnapshot(symbol="SRVR", name="ETF Data Centers & Infra", category="etf", period_return_pct=4.1),
            AssetSnapshot(symbol="XOP", name="ETF Pétrole & Gaz", category="etf", period_return_pct=4.9),
        ],
        macro_updates=[
            MacroIndicator(name="US CPI YoY", value=3.3, unit="%", previous_value=3.1, release_date=today),
            MacroIndicator(name="US Unemployment", value=4.0, unit="%", previous_value=3.9, release_date=today),
            MacroIndicator(name="US GDP (annualisé)", value=0.5, unit="%", previous_value=1.2, release_date=today),
            MacroIndicator(name="ECB Policy Rate", value=4.0, unit="%", previous_value=4.0, release_date=today),
        ],
        geopolitical_updates=[
            GeopoliticalEvent(
                title="Hausse des tensions au Moyen-Orient",
                source="Reuters",
                region="Middle East",
                date=today,
                impact_level="high",
                summary="Risque de perturbation logistique énergétique et prime de risque sur le pétrole.",
            ),
            GeopoliticalEvent(
                title="Relations commerciales USA/Chine sous surveillance",
                source="Reuters",
                region="Global",
                date=today,
                impact_level="medium",
                summary="Pression potentielle sur les chaînes d'approvisionnement technologiques.",
            ),
        ],
        risks=[
            "Inflation services persistante retardant un assouplissement monétaire rapide.",
            "Volatilité accrue des actifs risqués en cas d'escalade géopolitique.",
            "Sensibilité des valorisations growth à la hausse des taux longs.",
        ],
        opportunities=[
            "Renforcement progressif sur indices larges en cas de correction.",
            "Thématiques IA, cybersécurité et infrastructures numériques encore dynamiques.",
            "Diversification via actifs réels pour amortir le risque inflationniste.",
        ],
        business_highlights=[
            "Les publications bénéficiaires US restent globalement solides sur la tech et la qualité.",
            "Les banques d'investissement signalent une reprise graduelle de l'activité M&A.",
            "Les dépenses capex liées à l'IA soutiennent semi-conducteurs et data centers.",
        ],
    )


def run() -> Path:
    settings = load_settings()
    report = _build_placeholder_report()

    html_content = render_html_report(report)

    output_dir = Path("output")
    output_dir.mkdir(parents=True, exist_ok=True)

    html_file = output_dir / f"weekly_report_{report.period_end.isoformat()}.html"
    html_file.write_text(html_content, encoding="utf-8")

    print(f"Report generated: {html_file} | source_count={len(settings.sources)}")
    return html_file


if __name__ == "__main__":
    run()
