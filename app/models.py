from app import db

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(100))
    msg = db.Column(db.String(400))