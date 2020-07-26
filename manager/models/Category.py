from manager import db

class Category(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    # Genral Info
    name = db.Column(db.String(50), nullable=False)