"""
Modul pro definici objektů v knihovně.

Obsahuje třídy Literatura, Kniha a Časopis.
"""


class Literatura:
    """
    Třída reprezentující literaturu.

    Rodičovská třída pro knihu a časopis.
    Pokrývá všechny společné vlastnosti:
    název, rok vydání, počet výtisků,vhodnost pro děti, počet výpůjček.
    """

    def __init__(self, nazev: str, rok_vydani: int,
                 vhodna_pro_deti: bool = False,
                 pocet_vytisku: int = 1) -> None:
        """Konstruktor objektu."""
        self.nazev: str = nazev
        self.rok_vydani: int = rok_vydani
        self.pocet_vytisku: int = pocet_vytisku
        self.vhodna_pro_deti: bool = vhodna_pro_deti
        self.pocet_vypujcek = 0

    def vypujc(self) -> None:
        """Metoda pro výpůjčku knihy."""
        if self.pocet_vypujcek >= self.pocet_vytisku:
            raise ValueError("Všechny knihy jsou vypůjčené.")

        self.pocet_vypujcek += 1

    def vrat(self) -> None:
        """Metoda pro vrácení knihy."""
        if self.pocet_vypujcek == 0:
            raise ValueError("Žádná kniha není vypůjčená.")

        self.pocet_vypujcek -= 1


class Kniha(Literatura):
    """
    Třída reprezentující druh knihy knihu.

    Dědí od třídy Literatura. Přidává vlastnost autor.
    """

    def __init__(self,  # pylint: disable=too-many-arguments
                 nazev: str, autor: str, rok_vydani: int,
                 vhodna_pro_deti: bool = False, pocet_vytisku: int = 1) -> None:
        """Konstruktor objektu."""
        super().__init__(nazev=nazev, rok_vydani=rok_vydani, vhodna_pro_deti=vhodna_pro_deti,
                         pocet_vytisku=pocet_vytisku)
        self.autor: str = autor

    def __str__(self) -> str:
        """Metoda pro převod objektu na řetězec."""
        vypis: str = f"{self.nazev} od {self.autor} ({self.rok_vydani}), kusů: {self.pocet_vytisku},"\
                     f"vypůjčeno: {self.pocet_vypujcek}"
        if self.vhodna_pro_deti:
            vypis += " (vhodná pro děti)"
        return vypis


class Casopis(Literatura):
    """
    Třída reprezentující druh literatury - časopis.

    Dědí od třídy Literatura. Přidává vlastnost číslo.
    """

    def __init__(self,  # pylint: disable=too-many-arguments
                 nazev: str, rok_vydani: int, cislo: int,
                 vhodna_pro_deti: bool = False, pocet_vytisku: int = 1) -> None:
        """Konstruktor objektu."""
        super().__init__(nazev=nazev, rok_vydani=rok_vydani, vhodna_pro_deti=vhodna_pro_deti,
                         pocet_vytisku=pocet_vytisku)
        self.cislo: int = cislo

    def __str__(self) -> str:
        """Metoda pro převod objektu na řetězec."""
        vypis: str = f"{self.nazev} ({self.rok_vydani}), číslo {self.cislo}, kusů: {self.pocet_vytisku},"\
                     f"vypůjčeno: {self.pocet_vypujcek}"
        if self.vhodna_pro_deti:
            vypis += " (vhodná pro děti)"
        return vypis
