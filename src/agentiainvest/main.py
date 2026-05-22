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
            "Le scénario central reste constructif sur le long terme avec une progression des bénéfices, "
            "mais la combinaison taux élevés et tensions géopolitiques justifie une allocation graduelle et diversifiée."
        ),
        market_moves=[
            AssetSnapshot(symbol="SPX", name="S&P 500", category="index", period_return_pct=1.2),
            AssetSnapshot(symbol="NDX", name="NASDAQ 100", category="index", period_return_pct=2.1),
            AssetSnapshot(symbol="SXXP", name="STOXX Europe 600", category="index", period_return_pct=0.6),
            AssetSnapshot(symbol="NKY", name="Nikkei 225", category="index", period_return_pct=-0.4),
            AssetSnapshot(symbol="MXEF", name="MSCI Emerging Markets", category="index", period_return_pct=0.4),
            AssetSnapshot(symbol="CO1", name="Brent Pétrole", category="commodity", period_return_pct=3.2),
            AssetSnapshot(symbol="XAU", name="Or (USD/oz)", category="commodity", period_return_pct=0.7),
            AssetSnapshot(symbol="US10Y", name="US 10Y (variation hebdo)", category="bond", period_return_pct=0.05),
        ],
        remarkable_moves=[
            AssetSnapshot(symbol="IXN", name="MSCI World IT", category="etf", period_return_pct=3.0),
            AssetSnapshot(symbol="HACK", name="ETF Cybersécurité", category="etf", period_return_pct=4.1),
            AssetSnapshot(symbol="LUX", name="Indice Luxury Brands", category="equity", period_return_pct=-1.1),
            AssetSnapshot(symbol="SOXX", name="ETF Semi-conducteurs", category="etf", period_return_pct=3.8),
            AssetSnapshot(symbol="ICLN", name="ETF Énergie propre", category="etf", period_return_pct=1.4),
            AssetSnapshot(symbol="IXG", name="ETF Banques globales", category="etf", period_return_pct=1.0),
            AssetSnapshot(symbol="SRVR", name="ETF Data Centers & Infra", category="etf", period_return_pct=3.7),
            AssetSnapshot(symbol="XOP", name="ETF Pétrole & Gaz", category="etf", period_return_pct=4.4),
        ],
        quarterly_market_moves=[
            AssetSnapshot(symbol="SPX", name="S&P 500", category="index", period_return_pct=9.4),
            AssetSnapshot(symbol="NDX", name="NASDAQ 100", category="index", period_return_pct=12.8),
            AssetSnapshot(symbol="SXXP", name="STOXX Europe 600", category="index", period_return_pct=5.8),
            AssetSnapshot(symbol="NKY", name="Nikkei 225", category="index", period_return_pct=-1.1),
            AssetSnapshot(symbol="MXEF", name="MSCI Emerging Markets", category="index", period_return_pct=2.9),
            AssetSnapshot(symbol="CO1", name="Brent Pétrole", category="commodity", period_return_pct=14.2),
            AssetSnapshot(symbol="XAU", name="Or (USD/oz)", category="commodity", period_return_pct=11.7),
            AssetSnapshot(symbol="US10Y", name="US 10Y (variation 3 mois)", category="bond", period_return_pct=0.28),
        ],
        macro_updates=[
            MacroIndicator(name="Inflation US (CPI, a/a)", value=3.3, unit="%", previous_value=3.1, release_date=today),
            MacroIndicator(name="Emploi US (taux de chômage)", value=4.0, unit="%", previous_value=3.9, release_date=today),
        ],
        geopolitical_updates=[
            GeopoliticalEvent(
                title="Nouvelles tensions au Moyen-Orient",
                source="Reuters",
                region="Middle East",
                date=today,
                impact_level="high",
                summary="Le risque énergétique demeure une variable clé pour l'inflation importée.",
            )
        ],
        risks=["Volatilité énergie", "Risque taux", "Concentration marchés"],
        opportunities=["Qualité", "ETF diversifiés"],
        business_highlights=["Résultats solides"],
        geopolitical_narrative=[
            "Les tensions au Moyen Orient restent un facteur de volatilité sur l'énergie et entretiennent un biais prudent sur les actifs les plus sensibles à l'inflation.",
            "Les échanges commerciaux entre blocs restent sous surveillance et peuvent ralentir la normalisation des chaînes industrielles si de nouvelles restrictions apparaissent.",
            "En Europe la coordination budgétaire progresse lentement, ce qui soutient certains segments industriels mais n'efface pas les risques de croissance modérée."
        ],
        business_narrative=[
            "Les publications d'entreprises confirment une dynamique bénéficiaire robuste dans la technologie de qualité, avec une discipline de coûts plus visible qu'en début d'année.",
            "Les investissements liés à l'IA continuent de soutenir les fournisseurs de semi conducteurs, d'infrastructures cloud et de services de cybersécurité.",
            "Les secteurs financiers profitent encore d'un niveau de taux élevé, tandis que la reprise des opérations de marché reste progressive et sélective."
        ],
        risk_narrative=[
            "Une inflation de services encore ferme peut prolonger des conditions monétaires restrictives et maintenir une sensibilité élevée des valorisations de croissance.",
            "La hausse du pétrole pourrait se transmettre aux coûts de production et freiner la détente attendue sur les marges dans les secteurs cycliques.",
            "La concentration de performance sur un nombre réduit de mégacapitalisations impose une diversification plus stricte pour limiter le risque de rotation brutale."
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
