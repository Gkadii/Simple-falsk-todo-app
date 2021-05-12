from .database import db
from datetime import datetime


class Todo(db.Model):
    id      = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String(200), nullable = False)
    date    = db.Column(db.DateTime, default = datetime.utcnow)
    
    
    def __repr__(self):
        
        return f"task number is {self.id}"