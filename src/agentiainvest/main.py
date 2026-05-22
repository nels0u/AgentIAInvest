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
            "La tendance actions reste constructive grâce aux bénéfices et aux thématiques IA, "
            "mais le couple inflation/taux et la géopolitique énergie justifient une allocation progressive."
        ),
        market_moves=[
            AssetSnapshot(symbol="SPX", name="S&P 500", category="index", period_return_pct=1.4),
            AssetSnapshot(symbol="NDX", name="NASDAQ 100", category="index", period_return_pct=2.3),
            AssetSnapshot(symbol="SXXP", name="STOXX Europe 600", category="index", period_return_pct=0.7),
            AssetSnapshot(symbol="NKY", name="Nikkei 225", category="index", period_return_pct=-0.5),
            AssetSnapshot(symbol="MXEF", name="MSCI Emerging Markets", category="index", period_return_pct=0.5),
            AssetSnapshot(symbol="CO1", name="Brent Pétrole", category="commodity", period_return_pct=3.4),
            AssetSnapshot(symbol="XAU", name="Or (USD/oz)", category="commodity", period_return_pct=0.8),
            AssetSnapshot(symbol="US10Y", name="US 10Y (variation hebdo)", category="bond", period_return_pct=0.05),
        ],
        remarkable_moves=[
            AssetSnapshot(symbol="IXN", name="MSCI World IT", category="etf", period_return_pct=3.1),
            AssetSnapshot(symbol="HACK", name="ETF Cybersécurité", category="etf", period_return_pct=4.2),
            AssetSnapshot(symbol="LUX", name="Indice Luxury Brands", category="equity", period_return_pct=-1.0),
            AssetSnapshot(symbol="SOXX", name="ETF Semi-conducteurs", category="etf", period_return_pct=4.0),
            AssetSnapshot(symbol="ICLN", name="ETF Énergie propre", category="etf", period_return_pct=1.5),
            AssetSnapshot(symbol="IXG", name="ETF Banques globales", category="etf", period_return_pct=1.1),
            AssetSnapshot(symbol="SRVR", name="ETF Data Centers & Infra", category="etf", period_return_pct=3.9),
            AssetSnapshot(symbol="XOP", name="ETF Pétrole & Gaz", category="etf", period_return_pct=4.6),
        ],
        macro_updates=[
            MacroIndicator(name="Inflation US (CPI, a/a)", value=3.3, unit="%", previous_value=3.1, release_date=today),
            MacroIndicator(name="Emploi US (taux de chômage)", value=4.0, unit="%", previous_value=3.9, release_date=today),
            MacroIndicator(name="Croissance US (PIB annualisé)", value=0.6, unit="%", previous_value=1.3, release_date=today),
            MacroIndicator(name="Taux directeur BCE", value=4.0, unit="%", previous_value=4.0, release_date=today),
            MacroIndicator(name="PMI Manufacturier Monde", value=50.9, unit="pts", previous_value=50.4, release_date=today),
        ],
        geopolitical_updates=[
            GeopoliticalEvent(
                title="Nouvelles tensions au Moyen-Orient",
                source="Reuters",
                region="Middle East",
                date=today,
                impact_level="high",
                summary="Le risque sur les routes énergétiques renforce la prime de risque pétrole et les attentes inflationnistes.",
            ),
            GeopoliticalEvent(
                title="Resserrement commercial USA-Chine",
                source="Reuters",
                region="Global",
                date=today,
                impact_level="medium",
                summary="Hausse de l'incertitude sur la chaîne de valeur tech, avec impact potentiel sur marges et capex.",
            ),
            GeopoliticalEvent(
                title="Négociations budgétaires européennes",
                source="Financial Times",
                region="Europe",
                date=today,
                impact_level="low",
                summary="Visibilité en amélioration sur l'investissement infrastructurel, soutien graduel aux cycliques de qualité.",
            ),
        ],
        risks=[
            "Persistante inflation services : retard possible des baisses de taux directeurs.",
            "Énergie volatile : risque de compression des marges pour industries sensibles aux coûts.",
            "Valorisations growth exigeantes : sensibilité accrue aux surprises macro négatives.",
            "Concentration de performance sur méga-caps, augmentant le risque de rotation brutale.",
        ],
        opportunities=[
            "Renforcement progressif sur ETF larges en plusieurs points d'entrée.",
            "Exposition sélective aux thèmes IA/productivité avec discipline de valorisation.",
            "Diversification par actifs réels et qualité défensive pour réduire la volatilité.",
        ],
        business_highlights=[
            "La saison de résultats confirme une dynamique bénéficiaire solide sur la technologie de qualité.",
            "Les investissements IA soutiennent la demande en semi-conducteurs, cloud et infrastructures data.",
            "Les financières mondiales bénéficient d'un contexte de taux encore porteur pour les revenus d'intérêt.",
            "Les plans de capex industriels restent orientés modernisation/automatisation, soutien moyen terme à la productivité.",
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
