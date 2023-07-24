from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class Trainer(db.Model):
    trainer_id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(15))
    trainer_name = db.Column(db.String(20), nullable = False, unique = True)
    email = db.Column(db.String(70), nullable = False, unique = True)
    password_hash = db.Column(db.String(), nullable = False)
    poke_relate = db.relationship('Pokemon', backref = 'owner', lazy = True)

    def __repr__(self):
        return f'<TRAINER: {self.trainer_name}'
    
    def commit(self):
        db.session.add(self)
        db.session.commit()
                           
    def hash_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Pokemon(db.Model):
    pokemon_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    trainer_id = db.Column(db.Integer, db.ForeignKey('trainer.trainer_id'), nullable=False)
    
    def __repr__(self):
        return f'<Pokemon: {self.name}>'
    
    def commit(self):
        db.session.add(self)
        db.session.commit()

class TestTable(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)

class Test_Table(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)