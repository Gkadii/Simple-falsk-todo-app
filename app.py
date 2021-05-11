from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)
class Todo(db.Model):
    id      = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String(200), nullable = False)
    date    = db.Column(db.DateTime, default = datetime.utcnow)
    
    
    def __repr__(self):
        return f"task number is {self.id}"
      

@app.route('/',methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        # creating an new task to add 
        new_task = Todo(content = request.form.get('task'))
        #trying to add 
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return "err while adding try again"
        
        
    else:
        tasks = Todo.query.order_by(Todo.date)
        return render_template('index.html' , tasks=tasks)



   
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    #getting the task
    task = Todo.query.get_or_404(id)
    # changing the task contet
    if request.method =='POST':
        task.content = request.form.get('updating_task')
        #task.date    = datetime.utcnow
        
        try:
            db.session.commit()
            return redirect('/')
        except:
            return "<h1>sorry can't update and i don't know why</h1>"
    else:
        return render_template('update.html', task=task)

@app.route('/delete/<int:id>')
def remove(id):
    #get the task which we want to delete it 
    task = Todo.query.get_or_404(id)
    #deleting
    try:
        db.session.delete(task)
        db.session.commit()
    except:
        return "Nah can't be removed"
    return redirect('/')


if __name__=='__main__':
    app.run(debug=True)
    
 