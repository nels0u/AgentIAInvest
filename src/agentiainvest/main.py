from __future__ import annotations

from datetime import date, timedelta
from pathlib import Path

from .config import load_settings
from .models import AssetSnapshot, NarrativePoint, SourceLink, WeeklyReport
from .reporting import render_html_report


YAHOO_QUOTE = "https://finance.yahoo.com/quote/{symbol}"


def y(symbol: str) -> str:
    return YAHOO_QUOTE.format(symbol=symbol)


def _build_placeholder_report() -> WeeklyReport:
    today = date.today()
    start = today - timedelta(days=7)

    return WeeklyReport(
        period_start=start,
        period_end=today,
        generated_at=today,
        key_takeaway=(
            "La dynamique actions reste globalement favorable grâce à la qualité bénéficiaire, "
            "mais le niveau des taux réels et le risque énergétique imposent une allocation progressive et diversifiée."
        ),
        market_moves=[
            AssetSnapshot(symbol="^GSPC", name="S&P 500", category="index", period_return_pct=1.2, source_url=y("%5EGSPC")),
            AssetSnapshot(symbol="^NDX", name="NASDAQ 100", category="index", period_return_pct=2.1, source_url=y("%5ENDX")),
            AssetSnapshot(symbol="^STOXX", name="STOXX Europe 600", category="index", period_return_pct=0.6, source_url=y("%5ESTOXX")),
            AssetSnapshot(symbol="^N225", name="Nikkei 225", category="index", period_return_pct=-0.4, source_url=y("%5EN225")),
            AssetSnapshot(symbol="EEM", name="MSCI Emerging Markets (proxy ETF)", category="etf", period_return_pct=0.4, source_url=y("EEM")),
            AssetSnapshot(symbol="GLD", name="Or (proxy ETF)", category="etf", period_return_pct=0.7, source_url=y("GLD")),
            AssetSnapshot(symbol="USO", name="Pétrole (proxy ETF)", category="etf", period_return_pct=3.2, source_url=y("USO")),
            AssetSnapshot(symbol="TLT", name="US Treasuries long terme", category="etf", period_return_pct=-0.9, source_url=y("TLT")),
        ],
        remarkable_moves=[
            AssetSnapshot(symbol="SOXX", name="iShares Semiconductor ETF", category="etf", period_return_pct=3.8, source_url=y("SOXX")),
            AssetSnapshot(symbol="HACK", name="ETF Cybersécurité", category="etf", period_return_pct=4.1, source_url=y("HACK")),
            AssetSnapshot(symbol="SRVR", name="ETF Data Centers & Infra", category="etf", period_return_pct=3.7, source_url=y("SRVR")),
            AssetSnapshot(symbol="ICLN", name="ETF Énergie propre", category="etf", period_return_pct=1.4, source_url=y("ICLN")),
            AssetSnapshot(symbol="XLF", name="ETF Financières US", category="etf", period_return_pct=1.6, source_url=y("XLF")),
            AssetSnapshot(symbol="XLV", name="ETF Santé US", category="etf", period_return_pct=0.9, source_url=y("XLV")),
            AssetSnapshot(symbol="XLE", name="ETF Énergie US", category="etf", period_return_pct=4.4, source_url=y("XLE")),
            AssetSnapshot(symbol="ARKK", name="ETF Innovation", category="etf", period_return_pct=2.7, source_url=y("ARKK")),
        ],
        quarterly_market_moves=[
            AssetSnapshot(symbol="^GSPC", name="S&P 500", category="index", period_return_pct=9.4, source_url=y("%5EGSPC")),
            AssetSnapshot(symbol="^NDX", name="NASDAQ 100", category="index", period_return_pct=12.8, source_url=y("%5ENDX")),
            AssetSnapshot(symbol="^N225", name="Nikkei 225", category="index", period_return_pct=-1.1, source_url=y("%5EN225")),
            AssetSnapshot(symbol="EEM", name="Emerging Markets (proxy ETF)", category="etf", period_return_pct=2.9, source_url=y("EEM")),
            AssetSnapshot(symbol="GLD", name="Or (proxy ETF)", category="etf", period_return_pct=11.7, source_url=y("GLD")),
            AssetSnapshot(symbol="USO", name="Pétrole (proxy ETF)", category="etf", period_return_pct=14.2, source_url=y("USO")),
            AssetSnapshot(symbol="TLT", name="US Treasuries long terme", category="etf", period_return_pct=-3.0, source_url=y("TLT")),
        ],
        quarterly_remarkable_moves=[
            AssetSnapshot(symbol="SOXX", name="iShares Semiconductor ETF", category="etf", period_return_pct=22.4, source_url=y("SOXX")),
            AssetSnapshot(symbol="HACK", name="ETF Cybersécurité", category="etf", period_return_pct=16.7, source_url=y("HACK")),
            AssetSnapshot(symbol="SRVR", name="ETF Data Centers & Infra", category="etf", period_return_pct=19.3, source_url=y("SRVR")),
            AssetSnapshot(symbol="ICLN", name="ETF Énergie propre", category="etf", period_return_pct=8.5, source_url=y("ICLN")),
            AssetSnapshot(symbol="XLK", name="ETF Technologie US", category="etf", period_return_pct=18.4, source_url=y("XLK")),
            AssetSnapshot(symbol="XLI", name="ETF Industrielles US", category="etf", period_return_pct=7.9, source_url=y("XLI")),
            AssetSnapshot(symbol="XLF", name="ETF Financières US", category="etf", period_return_pct=11.3, source_url=y("XLF")),
            AssetSnapshot(symbol="XLE", name="ETF Énergie US", category="etf", period_return_pct=14.9, source_url=y("XLE")),
        ],
        macro_updates=[],
        geopolitical_updates=[],
        risks=[],
        opportunities=[],
        business_highlights=[],
        geopolitical_narrative=[
            NarrativePoint(
                text="Les tensions en zones de transit énergétique maintiennent une prime de risque sur le pétrole, ce qui renforce **la pression potentielle sur l'inflation importée**.",
                source=SourceLink(label="Reuters Middle East", url="https://www.reuters.com/world/middle-east/"),
            ),
            NarrativePoint(
                text="Le durcissement commercial entre grands blocs ralentit la normalisation de certaines chaînes industrielles avec un impact probable sur **les coûts de production technologiques**.",
                source=SourceLink(label="WTO", url="https://www.wto.org/"),
            ),
        ],
        business_narrative=[
            NarrativePoint(
                text="Les publications d'entreprises confirment une dynamique bénéficiaire solide avec **une meilleure discipline sur les marges opérationnelles**.",
                source=SourceLink(label="SEC EDGAR", url="https://www.sec.gov/edgar/search/"),
            ),
            NarrativePoint(
                text="La demande en infrastructure numérique soutient **les dépenses d'investissement en semi-conducteurs, cloud et cybersécurité**.",
                source=SourceLink(label="LSEG", url="https://www.lseg.com/en/data-analytics"),
            ),
        ],
        risk_narrative=[
            NarrativePoint(
                text="Une inflation de services encore élevée peut repousser l'assouplissement monétaire et accroître **la sensibilité des valorisations growth**.",
                source=SourceLink(label="Federal Reserve", url="https://www.federalreserve.gov/"),
            ),
            NarrativePoint(
                text="La concentration de la performance sur quelques mégacapitalisations exige **une diversification plus stricte** pour limiter le risque de rotation.",
                source=SourceLink(label="MSCI Research", url="https://www.msci.com/research-and-insights"),
            ),
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
