from __future__ import annotations

from pathlib import Path

import yaml
from pydantic import BaseModel


class SourceConfig(BaseModel):
    name: str
    type: str
    endpoint: str
    parser: str
    enabled: bool = True


class AgentSettings(BaseModel):
    timezone: str = "UTC"
    report_day: str = "sunday"
    report_hour_utc: int = 18
    lookback_days: int = 7
    sources: list[SourceConfig]


DEFAULT_CONFIG_PATH = Path("config/sources.yml")


def load_settings(path: Path = DEFAULT_CONFIG_PATH) -> AgentSettings:
    raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    return AgentSettings.model_validate(raw)
