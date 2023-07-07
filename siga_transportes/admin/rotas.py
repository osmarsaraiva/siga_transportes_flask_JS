from flask import render_template, session, request, redirect, url_for, flash

from loja import app, db, bcrypt
from .forms import RegistrationForm
import os

@app.route('/')
def home():
    return "Seja bem vindo"

@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
         user = User(form.username.data, form.email.data,
                     form.password.data)
        db_session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('admin/registrar.html', form=form, title="Pagina de registros")