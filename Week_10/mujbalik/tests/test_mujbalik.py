"""Testy pro mujbalik.py."""

from mujbalik import Knihovna, Kniha, Casopis, Dospely, Dite
import pytest


knihovna = Knihovna()


def test_inicializace_knihovny() -> None:
    """Test, zda se knihovna správně inicializuje."""
    list_knih: list[Kniha | Casopis] = []
    list_ctenaru: list[Dospely | Dite] = []

    kniha_tmp = Kniha(nazev="Kniha 1", autor="Autor 1", rok_vydani=2020, vhodna_pro_deti=False)
    knihovna.pridat_knihu(kniha=kniha_tmp)
    list_knih.append(kniha_tmp)

    kniha_tmp = Kniha(nazev="Kniha 2", autor="Autor 2", rok_vydani=2019, vhodna_pro_deti=False, pocet_vytisku=2)
    knihovna.pridat_knihu(kniha=kniha_tmp)
    list_knih.append(kniha_tmp)

    kniha_tmp = Kniha(nazev="Kniha 3", autor="Autor 3", rok_vydani=2023, vhodna_pro_deti=True)
    knihovna.pridat_knihu(kniha=kniha_tmp)
    list_knih.append(kniha_tmp)

    kniha_tmp = Casopis(nazev="Časopis 1", rok_vydani=2020, cislo=1, vhodna_pro_deti=False)
    knihovna.pridat_knihu(kniha=kniha_tmp)
    list_knih.append(kniha_tmp)

    kniha_tmp = Casopis(nazev="Časopis 2", rok_vydani=2021, cislo=2, vhodna_pro_deti=False, pocet_vytisku=2)
    knihovna.pridat_knihu(kniha=kniha_tmp)
    list_knih.append(kniha_tmp)

    kniha_tmp = Casopis(nazev="Časopis 3", rok_vydani=2022, cislo=1, vhodna_pro_deti=True)
    knihovna.pridat_knihu(kniha=kniha_tmp)
    list_knih.append(kniha_tmp)

    ctenar_tmp = Dospely(jmeno="Jan", prijmeni="Novák", ctenar_id=1)
    knihovna.pridat_ctenare(ctenar=ctenar_tmp)
    list_ctenaru.append(ctenar_tmp)

    ctenar_tmp = Dospely(jmeno="Petr", prijmeni="Novák", ctenar_id=2)
    knihovna.pridat_ctenare(ctenar=ctenar_tmp)
    list_ctenaru.append(ctenar_tmp)

    ctenar_tmp = Dite(jmeno="Jan", prijmeni="Novák", ctenar_id=3)
    knihovna.pridat_ctenare(ctenar=ctenar_tmp)
    list_ctenaru.append(ctenar_tmp)

    assert knihovna.knihy == list_knih

    assert knihovna.ctenari == list_ctenaru


def test_vypujcky_knih() -> None:
    """Test, zda se knihy správně vypůjčují."""
    knihovna.vypujcit_knihu(ctenar_id=1, kniha=Kniha(nazev="Kniha 1", autor="Autor 1", rok_vydani=2020))
    knihovna.vypujcit_knihu(ctenar_id=1, kniha=Casopis(nazev="Časopis 1", rok_vydani=2020, cislo=1))
    knihovna.vypujcit_knihu(ctenar_id=1, kniha=Kniha(nazev="Kniha 2", autor="Autor 2", rok_vydani=2019))
    knihovna.vypujcit_knihu(ctenar_id=2, kniha=Kniha(nazev="Kniha 2", autor="Autor 2", rok_vydani=2019))
    knihovna.vypujcit_knihu(ctenar_id=2, kniha=Casopis(nazev="Časopis 2", rok_vydani=2021, cislo=2))
    knihovna.vypujcit_knihu(ctenar_id=3, kniha=Kniha(nazev="Kniha 3", autor="Autor 3", rok_vydani=2023))
    knihovna.vypujcit_knihu(ctenar_id=3, kniha=Casopis(nazev="Časopis 3", rok_vydani=2022, cislo=1))


def test_vraceni_knih() -> None:
    """Test, zda se knihy správně vrací."""
    knihovna.vratit_knihu(ctenar_id=1, kniha=Kniha(nazev="Kniha 1", autor="Autor 1", rok_vydani=2020))
    knihovna.vratit_knihu(ctenar_id=1, kniha=Casopis(nazev="Časopis 1", rok_vydani=2020, cislo=1))
    knihovna.vratit_knihu(ctenar_id=1, kniha=Kniha(nazev="Kniha 2", autor="Autor 2", rok_vydani=2019))
    knihovna.vratit_knihu(ctenar_id=2, kniha=Kniha(nazev="Kniha 2", autor="Autor 2", rok_vydani=2019))
    knihovna.vratit_knihu(ctenar_id=3, kniha=Kniha(nazev="Kniha 3", autor="Autor 3", rok_vydani=2023))


def test_kontroly_neplatnych_vypujcek() -> None:
    """Test, zda se kontrolují neplatné výpůjčky."""
    with pytest.raises(expected_exception=ValueError):
        knihovna.vypujcit_knihu(ctenar_id=1, kniha=Casopis(nazev="Časopis 3", rok_vydani=2022, cislo=1))

    with pytest.raises(expected_exception=ValueError):
        knihovna.vypujcit_knihu(ctenar_id=1, kniha=Kniha(nazev="Kniha 4", autor="Autor 4", rok_vydani=2024))

    with pytest.raises(expected_exception=ValueError):
        knihovna.vypujcit_knihu(ctenar_id=3, kniha=Kniha(nazev="Kniha 1", autor="Autor 1", rok_vydani=2020))
