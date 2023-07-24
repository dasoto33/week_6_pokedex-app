from app import db

class Trainer(db.Model):
    trainer_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(15))
    trainer_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(70), nullable=False)
    password_hash = db.Column(db.String(), nullable=False)
    poke_relate = db.relationship('Pokemon', backref='owner', lazy=True)

    def __repr__(self):
        return f'<TRAINER: {self.trainer_name}'
    
    def commit(self):
        db.session.add(self)
        db.session.commit()
                           

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