"""
Modul pro definici uživatelů knihovny.

Obsahuje třídy Ctenar, Dospely a Dite.
"""

from typing import List
from .literatura import Kniha, Casopis


class Ctenar:
    """
    Třída reprezentující čtenáře.

    Rodičovská třída pro dospělého a dítěte.
    """

    def __init__(self, jmeno: str, prijmeni: str, ctenar_id: int):
        """Konstruktor objektu."""
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.ctenar_id = ctenar_id
        self.vypujcene_kusy: List[Kniha | Casopis] = []

    def __str__(self) -> str:
        """Metoda pro převod objektu na řetězec."""
        return f"{self.jmeno} {self.prijmeni} (ID: {self.ctenar_id}), \
počet vypůjčených kusů: {len(self.vypujcene_kusy)}"

    def vypujcit_knihu(self, kniha: Kniha | Casopis):
        """Metoda pro výpůjčku knihy."""
        self.vypujcene_kusy.append(kniha)

    def vratit_knihu(self, kniha: Kniha | Casopis):
        """Metoda pro vrácení knihy."""
        self.vypujcene_kusy.remove(kniha)

    def vypis_seznamu_vypujcenych_kusu(self):
        """Metoda pro výpis seznamu vypůjčených kusů."""
        print(f"Seznam vypůjčených kusů čtenáře {self.jmeno} {self.prijmeni}:")
        for kniha in self.vypujcene_kusy:
            print(kniha)


class Dospely(Ctenar):
    """Třída reprezentující dospělého čtenáře."""


class Dite(Ctenar):
    """Třída reprezentující dítě jako čtenáře."""

    def preved_na_dospeleho(self):
        """Metoda pro převod dítěte na dospělého."""
        novy_ucet = Dospely(self.jmeno, self.prijmeni, self.ctenar_id)
        novy_ucet.vypujcene_kusy = self.vypujcene_kusy
        return novy_ucet
