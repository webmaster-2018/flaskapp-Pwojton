#!/usr/bin/env python
# -- coding: utf-8 --

from flask_wtf import FlaskForm
from wtforms import HiddenField, StringField, BooleanField
from wtforms import SelectField, FormField, FieldList
from wtforms.validators import Required

blad_1 = 'To pole jest wymagane'

class DodajForm(FlaskForm):
    imie = StringField('Imie: ', validators=[Required(message="blad_1")])
    nazwisko = StringField('Nazwisko: ', validators=[Required(message="blad_1")])
    plec = SelectField('Płec: ', coerce=int)
    klasa = SelectField('Klasa: ', coerce=int)

    id = HiddenField()

class DodajKlasaForm(FlaskForm):
    klasa = StringField('Nazwę klasy: ', validators=[
                          Required(message="blad_1")])
    rok_naboru = StringField('rok naboru: ', validators=[
                          Required(message="blad_1")])
    rok_matury = StringField('rok matury: ', validators=[
                          Required(message="blad_1")])
