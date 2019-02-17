#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  modele.py

from peewee import *

baza_plik = 'baza.db'
baza = SqliteDatabase(baza_plik)  # instancja bazy

### MODELE #
class BazaModel(Model):
    class Meta:
        database = baza


class Klasa(BazaModel):
    nazwa = CharField(null=False)
    roknaboru = IntegerField(default=0)
    rokmatury = IntegerField(default=0)

    
class Uczen(BazaModel):
    imie = CharField(null=False)
    nazwisko = CharField(null=False)
    plec = ForeignKeyField(Klasa, related_name='plec')
    klasa = ForeignKeyField(Klasa, related_name='uczniowie')

class Plec(BazaModel):
	plec_rodzaj = CharField(null=False)

