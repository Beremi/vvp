"""Testy pro mujbalik.py."""

from mujbalik import Knihovna, Kniha, Casopis, Dospely, Dite
import pytest


knihovna = Knihovna()


def test_inicializace_knihovny():
    """Test, zda se knihovna správně inicializuje."""
    list_knih = []
    list_ctenaru = []

    kniha_tmp = Kniha("Kniha 1", "Autor 1", 2020, False)
    knihovna.pridat_knihu(kniha_tmp)
    list_knih.append(kniha_tmp)

    kniha_tmp = Kniha("Kniha 2", "Autor 2", 2019, False, pocet_vytisku=2)
    knihovna.pridat_knihu(kniha_tmp)
    list_knih.append(kniha_tmp)

    kniha_tmp = Kniha("Kniha 3", "Autor 3", 2023, True)
    knihovna.pridat_knihu(kniha_tmp)
    list_knih.append(kniha_tmp)

    kniha_tmp = Casopis("Časopis 1", 2020, 1, False)
    knihovna.pridat_knihu(kniha_tmp)
    list_knih.append(kniha_tmp)

    kniha_tmp = Casopis("Časopis 2", 2021, 2, False, pocet_vytisku=2)
    knihovna.pridat_knihu(kniha_tmp)
    list_knih.append(kniha_tmp)

    kniha_tmp = Casopis("Časopis 3", 2022, 1, True)
    knihovna.pridat_knihu(kniha_tmp)
    list_knih.append(kniha_tmp)

    ctenar_tmp = Dospely("Jan", "Novák", 1)
    knihovna.pridat_ctenare(ctenar_tmp)
    list_ctenaru.append(ctenar_tmp)

    ctenar_tmp = Dospely("Petr", "Novák", 2)
    knihovna.pridat_ctenare(ctenar_tmp)
    list_ctenaru.append(ctenar_tmp)

    ctenar_tmp = Dite("Jan", "Novák", 3)
    knihovna.pridat_ctenare(ctenar_tmp)
    list_ctenaru.append(ctenar_tmp)

    assert knihovna.knihy == list_knih

    assert knihovna.ctenari == list_ctenaru


def test_vypujcky_knih():
    """Test, zda se knihy správně vypůjčují."""
    knihovna.vypujcit_knihu(1, Kniha("Kniha 1", "Autor 1", 2020))
    knihovna.vypujcit_knihu(1, Casopis("Časopis 1", 2020, 1))
    knihovna.vypujcit_knihu(1, Kniha("Kniha 2", "Autor 2", 2019))
    knihovna.vypujcit_knihu(2, Kniha("Kniha 2", "Autor 2", 2019))
    knihovna.vypujcit_knihu(2, Casopis("Časopis 2", 2021, 2))
    knihovna.vypujcit_knihu(3, Kniha("Kniha 3", "Autor 3", 2023))
    knihovna.vypujcit_knihu(3, Casopis("Časopis 3", 2022, 1))


def test_vraceni_knih():
    """Test, zda se knihy správně vrací."""
    knihovna.vratit_knihu(1, Kniha("Kniha 1", "Autor 1", 2020))
    knihovna.vratit_knihu(1, Casopis("Časopis 1", 2020, 1))
    knihovna.vratit_knihu(1, Kniha("Kniha 2", "Autor 2", 2019))
    knihovna.vratit_knihu(2, Kniha("Kniha 2", "Autor 2", 2019))
    knihovna.vratit_knihu(3, Kniha("Kniha 3", "Autor 3", 2023))


def test_kontroly_neplatnych_vypujcek():
    """Test, zda se kontrolují neplatné výpůjčky."""
    with pytest.raises(ValueError):
        knihovna.vypujcit_knihu(1, Casopis("Časopis 3", 2022, 1))

    with pytest.raises(ValueError):
        knihovna.vypujcit_knihu(1, Kniha("Kniha 4", "Autor 4", 2024))

    with pytest.raises(ValueError):
        knihovna.vypujcit_knihu(3, Kniha("Kniha 1", "Autor 1", 2020))
