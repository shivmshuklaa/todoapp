from flask import Flask, render_template, redirect, url_for, request
from flask_mongoengine import MongoEngine
from models.todolist import TodoList

# creating app
app = Flask(__name__)

# configuring mongodb
app.config['MONGODB_SETTINGS'] = {
    'db': 'test',
    'host': 'mongodb+srv://admin:12345@cluster0.c2xkg5j.mongodb.net/?retryWrites=true&w=majority'
}

# connecting to mongodb
db = MongoEngine()
db.init_app(app)

# routes


@app.route('/')
def index():
    return render_template('index.html', items=TodoList.objects)


@app.route('/add', methods=['POST'])
def add():
    task = TodoList(task=request.form['task'])
    task.save()
    return redirect(url_for('index'))


@app.route('/done', methods=['GET'])
def done():
    task = TodoList.objects(task=request.args['task'])
    task.update(complete=True)
    return redirect(url_for('index'))


@app.route('/delete', methods=['GET'])
def delete():
    if request.args['key'] == 'completed':
        completed_tasks = TodoList.objects(complete=True)
        completed_tasks.delete()
    else:
        TodoList.drop_collection()
    return redirect(url_for('index'))
