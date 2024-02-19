
# -*- coding: utf8 -*-
from auto import Auto
import pytest

def test_vypocet_spotreby():
    auto = Auto(10, 200)                   # Dost žere, ale je rychlé
    nadrz1 = auto.nadrz
    auto.ujed(100)
    nadrz2 = auto.nadrz
    assert 10 == nadrz1 - nadrz2           # Víme, že auto mělo spotřebovat 10 litrů

def test_neprazdna_nadrz():
    auto = Auto(8, 100)
    with pytest.raises(Exception):
        auto.ujed(1000)                    # Dojde benzín
    assert auto.nadrz == 0                 # I poté musí nádrž být nejhůře prázdná    

def test_nesmyslnych_aut():
    with pytest.raises(Exception):
        auto = Auto(0, 100)                # Auto bez spotřeby!
    with pytest.raises(Exception):
        auto = Auto(10, 0)                 # Auto, které neumí jezdit!
    with pytest.raises(Exception):
        auto = Auto(-10, 100)              # Auto, které vyrábí benzín.

def test_nezaporna_vzdalenost():       # Metody začínající na "test_" jsou automaticky spuštěny
    auto = Auto(8, 100)
    with pytest.raises(Exception):
        auto.ujed(-1)
