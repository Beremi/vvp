
# -*- coding: utf8 -*-
from __future__ import division

class Auto(object):
    def __init__(self, spotreba, rychlost):
        if spotreba <= 0:
            raise Exception("Auto musí mít nezápornou spotřebu.")
        if rychlost <= 0:
            raise Exception("Auto musí jezdit nezápornou rychlostí.")
        self.spotreba = spotreba
        self.rychlost = rychlost
        self.cas = 0
        self.vzdalenost = 0
        self.nadrz = 50
        
    def ujed(self, vzdalenost):
        if vzdalenost < 0:
            raise Exception("Vzdálenost musí být nezáporná.")
        if (vzdalenost * self.spotreba / 100) > self.nadrz:
            # Auto ujede, kolik může a pak vyhodí výjimku
            skutecna_vzdalenost = 100 * (self.nadrz / self.spotreba) 
            self.ujed(skutecna_vzdalenost)    # Rekurze :-)
            raise Exception("Došel benzín")
        self.vzdalenost += vzdalenost
        self.cas += vzdalenost / self.rychlost
        self.nadrz -= (vzdalenost * self.spotreba / 100)
