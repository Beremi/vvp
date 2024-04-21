"""
Modul pro definici Knihovny.

Slouží k evidenci knih a čtenářů.
"""

from typing import List
from .literatura import Kniha, Casopis
from .ucty import Dospely, Dite


class Knihovna:
    """
    Třída reprezentující knihovnu.

    Obsahuje seznam knih a čtenářů.
    Umožňuje přidávat knihy a čtenáře, vypůjčovat a vracet knihy.
    """

    def __init__(self) -> None:
        """Konstruktor objektu."""
        self.knihy: List[Kniha | Casopis] = []
        self.ctenari: List[Dospely | Dite] = []

    def pridat_knihu(self, kniha: Kniha | Casopis) -> None:
        """Přidá knihu do seznamu knih."""
        self.knihy.append(kniha)

    def pridat_ctenare(self, ctenar: Dospely | Dite) -> None:
        """Přidá čtenáře do seznamu čtenářů."""
        self.ctenari.append(ctenar)

    def vypujcit_knihu(self, ctenar_id: int, kniha: Kniha | Casopis) -> None:
        """Vypůjčí knihu čtenáři."""
        ctenar: Dospely | Dite | None = self._najit_ctenare(ctenar_id=ctenar_id)
        if not ctenar:
            raise ValueError("Čtenář neexistuje.")

        kniha_v_knihovne: Kniha | Casopis | None = self._najit_knihu(kniha=kniha)
        if not kniha_v_knihovne:
            raise ValueError("Kniha/časopis není v knihovně.")

        if (not kniha_v_knihovne.vhodna_pro_deti) and \
                isinstance(ctenar, Dite):
            raise ValueError("Kniha/časopis není vhodná pro děti.")

        kniha_v_knihovne.vypujc()
        ctenar.vypujcit_knihu(kniha=kniha_v_knihovne)

    def vratit_knihu(self, ctenar_id: int, kniha: Kniha | Casopis) -> None:
        """Vrátí knihu od čtenáře."""
        ctenar: Dospely | Dite | None = self._najit_ctenare(ctenar_id=ctenar_id)
        if not ctenar:
            raise ValueError("Čtenář neexistuje.")

        kniha_v_knihovne: Kniha | Casopis | None = self._najit_knihu(kniha=kniha)
        if not kniha_v_knihovne:
            raise ValueError("Kniha/časopis není v knihovně.")

        kniha_v_knihovne.vrat()
        ctenar.vratit_knihu(kniha=kniha_v_knihovne)

    def _najit_ctenare(self, ctenar_id: int) -> Dospely | Dite | None:
        """Najde čtenáře podle ID."""
        for ctenar in self.ctenari:
            if ctenar.ctenar_id == ctenar_id:
                return ctenar
        return None

    def _najit_knihu(self, kniha: Kniha | Casopis) -> Kniha | Casopis | None:
        """Najde knihu dle názvu a roku vydání."""
        for kniha_v_knihovne in self.knihy:
            if kniha_v_knihovne.nazev == kniha.nazev and kniha_v_knihovne.rok_vydani == kniha.rok_vydani:
                return kniha_v_knihovne
        return None

    def __str__(self) -> str:
        """Vrátí textovou reprezentaci objektu."""
        return f"Knihovna obsahuje {len(self.knihy)} knih a {len(self.ctenari)} čtenářů."

    def vypsat_knihy(self) -> None:
        """Vypíše seznam knih."""
        print("-----------------------")
        print("Seznam knih v knihovně:")
        for kniha in self.knihy:
            print(kniha)
        print("-----------------------")

    def vypsat_ctenare(self) -> None:
        """Vypíše seznam čtenářů."""
        print("-----------------------")
        print("Seznam čtenářů knihovny:")
        for ctenar in self.ctenari:
            print(ctenar)
        print("-----------------------")

    def vypsat_vypujcene_knihy(self) -> None:
        """Vypíše seznam vypůjčených knih."""
        print("-----------------------")
        print("Seznam výpůjček:")
        for ctenar in self.ctenari:
            ctenar.vypis_seznamu_vypujcenych_kusu()
        print("-----------------------")
