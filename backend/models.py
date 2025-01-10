from database import db

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True) #Unique Identifier
    title = db.Column(db.String(250), nullable=False) #What you want to do
    completed = db.Column(db.Boolean, default = False)# The status of the task whether completed or not


    def __repr__(self):
        return f'<Todo {self.id} - {self.title}>'