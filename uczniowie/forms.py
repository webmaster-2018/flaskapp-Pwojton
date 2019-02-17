# -*- coding: utf-8 -*-
# quiz-orm/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, HiddenField, FieldList
from wtforms import SelectField, FormField, BooleanField
from wtforms.validators import Required

blad1 = 'To pole jest wymagane'


class KlasaForm(FlaskForm):
    id = HiddenField()
    nazwa = StringField('Klasa:', validators =[Required(message=blad1)])
    rok_naboru = StringField('Rok naboru:', validators =[Required(message=blad1)])
    rok_matury = StringField('Rok matury:', validators =[Required(message=blad1)])
    


class UczenForm(FlaskForm):
    id = HiddenField()
    imie = StringField('Imie:', validators =[Required(message=blad1)])
    nazwisko = StringField('Nazwisko:', validators =[Required(message=blad1)])
    plec = SelectField('Plec:',  coerce=int)
    klasa = SelectField('Klasa:',  coerce=int)
