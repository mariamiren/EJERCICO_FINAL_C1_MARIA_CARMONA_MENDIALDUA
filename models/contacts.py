from utils.db import db

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    phone = db.Column(db.String(15))
    
    def __init__(self, name, email, phone):
         self.name = name
         self.email = email
         self.phone = phone
         