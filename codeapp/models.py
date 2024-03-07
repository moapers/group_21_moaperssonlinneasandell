from __future__ import annotations

# python built-in imports
from dataclasses import dataclass
from datetime import date


@dataclass
class Sales:
    order_id: int
    country: str
    item_type: str
    order_priority: str
    order_date: date
    ship_date: date
    units_sold: int
    profit: float
