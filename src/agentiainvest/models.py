from __future__ import annotations

from datetime import date
from typing import Literal

from pydantic import BaseModel, Field


class AssetSnapshot(BaseModel):
    symbol: str
    name: str
    category: Literal["index", "etf", "equity", "bond", "commodity", "fx", "crypto"]
    period_return_pct: float
    previous_period_return_pct: float | None = None


class MacroIndicator(BaseModel):
    name: str
    value: float
    unit: str
    release_date: date
    previous_value: float | None = None


class GeopoliticalEvent(BaseModel):
    title: str
    source: str
    region: str
    date: date
    impact_level: Literal["low", "medium", "high"]
    summary: str


class HighlightSection(BaseModel):
    title: str
    bullets: list[str]


class WeeklyReport(BaseModel):
    period_start: date
    period_end: date
    generated_at: date
    key_takeaway: str = Field(..., min_length=20)
    market_moves: list[AssetSnapshot]
    remarkable_moves: list[AssetSnapshot] = Field(default_factory=list)
    macro_updates: list[MacroIndicator]
    geopolitical_updates: list[GeopoliticalEvent]
    risks: list[str]
    opportunities: list[str]
    business_highlights: list[str] = Field(default_factory=list)
