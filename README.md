# AgentIAInvest

Agent IA orienté **veille macroéconomique, marchés financiers et géopolitique** pour produire un rapport hebdomadaire structuré utilisable comme support d'investissement long terme.

## Ce que fait ce socle
- Charge une configuration de sources officielles (macro, filings, news).
- Normalise les données dans des modèles typés (`pydantic`).
- Génère un rapport hebdomadaire en **HTML (email-ready)** via template Jinja.
- Prépare l'automatisation (cron/GitHub Actions) pour une génération récurrente.

## Démarrage rapide
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
PYTHONPATH=src python -m agentiainvest.main
```

Le rapport est exporté dans `output/weekly_report_YYYY-MM-DD.html`.

## Rendu visuel type "synthèse marché"
Le template HTML (`prompts/weekly_report.html.j2`) suit une structure proche de votre exemple :
- en-tête fort avec période analysée,
- deux panneaux de données (marchés + macro),
- trois cartes de contexte (géopolitique, business, points d'attention),
- section "À retenir" en bas de page.

## Architecture recommandée (prochaine étape)
1. **Ingestion**: connecter les parseurs réels pour FRED/BLS/ECB/SEC + news géopolitiques.
2. **Feature engineering**: variations WoW, MoM, surprises vs consensus, régimes de volatilité.
3. **Raisonnement IA**: LLM + garde-fous (sources citées, scoring d'incertitude, hypothèses explicites).
4. **Publication**: push email/Notion/PDF + archivage versionné.
5. **Scheduler**: exécution hebdomadaire (dimanche 18:00 UTC).

## Exemple d'automatisation cron
```cron
0 18 * * 0 cd /workspace/AgentIAInvest && PYTHONPATH=src /usr/bin/python3 -m agentiainvest.main
```

## Note importante
Ce projet produit un support d'information et **ne remplace pas** un conseil financier professionnel.
