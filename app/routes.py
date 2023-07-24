from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm, RegisterForm
from app.models import Trainer


@app.route('/')
def home():
    pokedex_posts = {
        'trainers': {
            'david': ['WonK Machine']
        },
        'pokemon': {pokemon:f'This is my {num} pokemon' for num,pokemon in enumerate(['charizard', 'squirtle', 'pikachu'])}
    }
    return render_template('index.jinja', trainers=pokedex_posts['trainers'], pokemon=pokedex_posts['pokemon'])

@app.route('/signin/', methods=['GET', 'POST'])
def sign_in():
   login_form = LoginForm()
   if login_form.validate_on_submit():
       email = login_form.email.data
       trainer = Trainer.query.filter_by(email=email).first()
       if trainer and trainer.check_password(login_form.password.data):
            flash(f'{login_form.email.data} logged in!', category='success')
            return redirect('/')
       else:
           flash(f'Invalid login, please try again.', category='warning')
   return render_template('signin.jinja', form=login_form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        first_name = form.first_name.data
        trainer_name = form.trainer_name.data
        email = form.email.data
        password = form.password.data
        trainer = Trainer(first_name=first_name, trainer_name=trainer_name, email=email)
        trainer.hash_password(form.password.data)
        trainer.commit()
        flash(f'{first_name if first_name else trainer_name} registered', category='success')
        return redirect('/')
    return render_template('register.jinja', form=form)