"""
Toto je balíček mujbalik.

Obsahuje moduly:
- ucty - obsahuje třídy pro uživatele knihovny
- knihovna - obsahuje třídu pro knihovnu
- kniha - obsahuje třídy pro knihy a časopisy

Pro uživatelské rozhraní použijte přímo třídy:
- Dospely - reprezentuje dospělého čtenáře
- Dite - reprezentuje dítě jako čtenáře (s omezením na výpůjčku)
- Knihovna - reprezentuje knihovnu
- Kniha - reprezentuje knihu jako typ literatury k výpůjčce
- Casopis - reprezentuje časopis jako typ literatury k výpůjčce
"""

from .literatura import Kniha, Casopis
from .ucty import Dospely, Dite
from .knihovna import Knihovna

__all__: list[str] = ["Kniha", "Casopis", "Dospely", "Dite", "Knihovna"]
