# -*- coding: utf-8 -*-
# quiz-orm/views.py

from flask import Flask
from flask import render_template, request, redirect, url_for, abort, flash
from modele import *
from forms import *

app = Flask(__name__)

@app.route('/')
def index():
    """Strona główna"""
    return render_template('index.html')

@app.route("/lista")
def lista():
    uczen = Uczen.select()
    return render_template('lista.html', uczen=uczen)


@app.route("/dodaj", methods=['GET', 'POST'])
def dodaj():
    """Dodwanie pytań i odpowiedzi"""
    form = UczenForm()
    form.klasa.choices = [(k.id, k.klasa) for k in Klasa.select()]

    if form.validate_on_submit():
        print(form.data)
        p = Uczen(imie=form.imie.data, nazwisko=form.nazwisko.data, plec=form.plec.data)
        p.save()
        for o in form.odpowiedzi.data:
            odp = Odpowiedz(odpowiedz=o['odpowiedz'],
                            pytanie=p.id,
                            odpok=int(o['odpok']))
            odp.save()
        flash("Dodano ucznia: {}".format(form.uczen.data))
        return redirect(url_for('lista'))
        
    elif request.method == 'POST':
        flash_errors(form)
    
    return render_template('dodaj.html', form=form)
