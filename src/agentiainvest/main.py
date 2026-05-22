from __future__ import annotations

from datetime import date, timedelta
from pathlib import Path

from .config import load_settings
from .models import (
    AssetSnapshot,
    GeopoliticalEvent,
    MacroIndicator,
    NarrativePoint,
    SourceLink,
    WeeklyReport,
)
from .reporting import render_html_report


def _build_placeholder_report() -> WeeklyReport:
    today = date.today()
    start = today - timedelta(days=7)

    return WeeklyReport(
        period_start=start,
        period_end=today,
        generated_at=today,
        key_takeaway=(
            "Le socle de performance reste orienté positivement, avec une dynamique bénéficiaire solide, "
            "mais le couple inflation énergie et sensibilité aux taux impose une allocation disciplinée."
        ),
        market_moves=[
            AssetSnapshot(symbol="SPX", name="S&P 500", category="index", period_return_pct=1.2, source_url="https://www.spglobal.com/spdji/en/indices/equity/sp-500/"),
            AssetSnapshot(symbol="NDX", name="NASDAQ 100", category="index", period_return_pct=2.1, source_url="https://www.nasdaq.com/market-activity/index/ndx"),
            AssetSnapshot(symbol="SXXP", name="STOXX Europe 600", category="index", period_return_pct=0.6, source_url="https://www.stoxx.com/index-details?symbol=SXXP"),
            AssetSnapshot(symbol="NKY", name="Nikkei 225", category="index", period_return_pct=-0.4, source_url="https://indexes.nikkei.co.jp/en/nkave/index/profile"),
            AssetSnapshot(symbol="MXEF", name="MSCI Emerging Markets", category="index", period_return_pct=0.4, source_url="https://www.msci.com/www/index-factsheets/msci-emerging-markets-index/070542"),
        ],
        remarkable_moves=[
            AssetSnapshot(symbol="SOXX", name="iShares Semiconductor ETF", category="etf", period_return_pct=3.8, source_url="https://www.ishares.com/us/products/239705/ishares-phlx-semiconductor-etf"),
            AssetSnapshot(symbol="HACK", name="ETF Cybersécurité", category="etf", period_return_pct=4.1, source_url="https://www.etf.com/HACK"),
            AssetSnapshot(symbol="SRVR", name="ETF Data Centers & Infra", category="etf", period_return_pct=3.7, source_url="https://www.etf.com/SRVR"),
            AssetSnapshot(symbol="ICLN", name="ETF Énergie propre", category="etf", period_return_pct=1.4, source_url="https://www.ishares.com/us/products/239738/ishares-global-clean-energy-etf"),
            AssetSnapshot(symbol="XOP", name="ETF Pétrole & Gaz", category="etf", period_return_pct=4.4, source_url="https://www.ssga.com/us/en/intermediary/etfs/funds/the-energy-select-sector-spdr-fund-xle"),
        ],
        quarterly_market_moves=[
            AssetSnapshot(symbol="SPX", name="S&P 500", category="index", period_return_pct=9.4, source_url="https://www.spglobal.com/spdji/en/indices/equity/sp-500/"),
            AssetSnapshot(symbol="NDX", name="NASDAQ 100", category="index", period_return_pct=12.8, source_url="https://www.nasdaq.com/market-activity/index/ndx"),
            AssetSnapshot(symbol="SXXP", name="STOXX Europe 600", category="index", period_return_pct=5.8, source_url="https://www.stoxx.com/index-details?symbol=SXXP"),
            AssetSnapshot(symbol="NKY", name="Nikkei 225", category="index", period_return_pct=-1.1, source_url="https://indexes.nikkei.co.jp/en/nkave/index/profile"),
            AssetSnapshot(symbol="MXEF", name="MSCI Emerging Markets", category="index", period_return_pct=2.9, source_url="https://www.msci.com/www/index-factsheets/msci-emerging-markets-index/070542"),
        ],
        quarterly_remarkable_moves=[
            AssetSnapshot(symbol="SOXX", name="iShares Semiconductor ETF", category="etf", period_return_pct=22.4, source_url="https://www.ishares.com/us/products/239705/ishares-phlx-semiconductor-etf"),
            AssetSnapshot(symbol="HACK", name="ETF Cybersécurité", category="etf", period_return_pct=16.7, source_url="https://www.etf.com/HACK"),
            AssetSnapshot(symbol="SRVR", name="ETF Data Centers & Infra", category="etf", period_return_pct=19.3, source_url="https://www.etf.com/SRVR"),
            AssetSnapshot(symbol="ICLN", name="ETF Énergie propre", category="etf", period_return_pct=8.5, source_url="https://www.ishares.com/us/products/239738/ishares-global-clean-energy-etf"),
            AssetSnapshot(symbol="XOP", name="ETF Pétrole & Gaz", category="etf", period_return_pct=14.9, source_url="https://www.ssga.com/us/en/intermediary/etfs/funds/the-energy-select-sector-spdr-fund-xle"),
        ],
        macro_updates=[
            MacroIndicator(name="Inflation US (CPI, a/a)", value=3.3, unit="%", previous_value=3.1, release_date=today, source_url="https://www.bls.gov/cpi/"),
            MacroIndicator(name="Emploi US (taux de chômage)", value=4.0, unit="%", previous_value=3.9, release_date=today, source_url="https://www.bls.gov/cps/"),
        ],
        geopolitical_updates=[
            GeopoliticalEvent(
                title="Nouvelles tensions au Moyen-Orient",
                source="Reuters",
                region="Middle East",
                date=today,
                impact_level="high",
                summary="Le risque énergétique demeure une variable clé pour l'inflation importée.",
                source_url="https://www.reuters.com/world/middle-east/",
            )
        ],
        risks=["Volatilité énergie", "Risque taux", "Concentration marchés"],
        opportunities=["Qualité", "ETF diversifiés"],
        business_highlights=["Résultats solides"],
        geopolitical_narrative=[
            NarrativePoint(
                text="Les tensions en zones de transit énergétique maintiennent une prime de risque sur le pétrole, ce qui renforce **la pression potentielle sur l'inflation importée**.",
                source=SourceLink(label="Reuters Middle East", url="https://www.reuters.com/world/middle-east/"),
            ),
            NarrativePoint(
                text="Le durcissement commercial entre grands blocs ralentit la normalisation de certaines chaînes industrielles, avec un impact probable sur **les coûts de production technologiques**.",
                source=SourceLink(label="OMC Trade Monitoring", url="https://www.wto.org/english/res_e/statis_e/trade_datasets_e.htm"),
            ),
        ],
        business_narrative=[
            NarrativePoint(
                text="Les publications récentes indiquent une dynamique bénéficiaire globalement solide sur les segments qualité, avec **une meilleure discipline sur les marges opérationnelles**.",
                source=SourceLink(label="SEC EDGAR", url="https://www.sec.gov/edgar/search/"),
            ),
            NarrativePoint(
                text="La demande en infrastructure numérique continue de progresser, soutenant **les dépenses d'investissement en semi-conducteurs, cloud et cybersécurité**.",
                source=SourceLink(label="LSEG Earnings", url="https://www.lseg.com/en/data-analytics"),
            ),
        ],
        risk_narrative=[
            NarrativePoint(
                text="Une inflation de services encore élevée peut repousser le calendrier d'assouplissement monétaire et augmenter **la sensibilité des valorisations growth**.",
                source=SourceLink(label="Federal Reserve", url="https://www.federalreserve.gov/monetarypolicy.htm"),
            ),
            NarrativePoint(
                text="La concentration de la performance sur peu de mégacapitalisations justifie une diversification renforcée afin de réduire **le risque de rotation brutale**.",
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
