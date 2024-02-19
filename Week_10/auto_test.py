
# -*- coding: utf8 -*-
from auto import Auto
import unittest

class AutoTest(unittest.TestCase):             # Dědíme z třídy unittest.TestCase
    def test_vypocet_spotreby(self):
        auto = Auto(10, 200)                   # Dost žere, ale je rychlé
        nadrz1 = auto.nadrz
        auto.ujed(100)
        nadrz2 = auto.nadrz
        self.assertEqual(10, nadrz1 - nadrz2)  # Víme, že auto mělo spotřebovat 10 litrů
        
    def test_neprazdna_nadrz(self):
        auto = Auto(8, 100)
        with self.assertRaises(Exception):
            auto.ujed(1000)                    # Dojde benzín
        self.assertTrue(auto.nadrz == 0)       # I poté musí nádrž být nejhůře prázdná    
        
    def test_nesmyslnych_aut(self):
        with self.assertRaises(Exception):
            auto = Auto(0, 100)                # Auto bez spotřeby!
        with self.assertRaises(Exception):
            auto = Auto(10, 0)                 # Auto, které neumí jezdit!
        with self.assertRaises(Exception):
            auto = Auto(-10, 100)              # Auto, které vyrábí benzín.

    def test_nezaporna_vzdalenost(self):       # Metody začínající na "test_" jsou automaticky spuštěny
        auto = Auto(8, 100)
        with self.assertRaises(Exception):
            auto.ujed(-1)
    
if __name__ == "__main__":
    unittest.main()                 # Tímto pustíme testy
