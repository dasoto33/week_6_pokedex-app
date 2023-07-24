from flask import render_template
from app import app
from app.forms import LoginForm



@app.route('/')
def home():
    pokedex_posts = {
        'trainers': {
            'david': ['WonK Machine']
        },
        'pokemon': {pokemon:f'This is my {num} pokemon' for num,pokemon in enumerate(['charizard', 'squirtle', 'pikachu'])}
    }
    return render_template('index.jinja', trainers=pokedex_posts['trainers'], pokemon=pokedex_posts['pokemon'])

@app.route('/signin/')
def sign_in():
   form = LoginForm()
   return render_template('signin.jinja', form=form)

@app.route('/register')
def register():
    return render_template('register.jinja')