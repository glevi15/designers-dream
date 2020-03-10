import gridfs
from flask import Flask, jsonify, request, render_template
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://127.0.0.1:27017")
db = client.designer_db
tasks_collection = db.sketches

initial_tasks = [task for task in tasks_collection.find()]

if (len(initial_tasks)) == 0:
    tasks_collection.insert({
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    })
    tasks_collection.insert({
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    })


@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    all_tasks = tasks_collection.find()
    task_list = []
    for task in all_tasks:
        task_list.append({'title': task['title'], 'description': task['description'], 'id': task['id']})

    return jsonify({'tasks': task_list})


@app.route('/api/create-task', methods=['GET'])
def create_task():
    tasks = tasks_collection.find()
    new_task = {"id": tasks.count(), "title": "Learn Mongo", "description": "Start with Flask + Mongo", "done": False}
    tasks_collection.insert(new_task)
    all_tasks = tasks_collection.find()
    task_list = []
    for task in all_tasks:
        task_list.append({'title': task['title'], 'description': task['description'], 'id': task['id']})
    return jsonify({'tasks': task_list})


@app.route('/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    tasks = tasks_collection.find({'id': task_id})
    if tasks.count() == 0:
        return jsonify({'task': None})
    return jsonify({'task': tasks[0]})


@app.route('/', methods=['GET'])
def home():
    return jsonify({'msg': 'This is the Home'})


@app.route('/test', methods=['GET'])
def test():
    return jsonify({'msg': 'This is a Test'})


@app.route('/get-file/<name>')
@app.route('/get-file')
def get_file(name=None):
    fs = gridfs.GridFS(MongoClient().CINEfs_example)

    if name is not None:
        f = fs.get_last_version(name)
        r = app.response_class(f, direct_passthrough=True, mimetype='application/octet-stream')
        r.headers.set('Content-Disposition', 'attachment', filename=name)
        return r

    return render_template('get_file.html', names=fs.list())


if __name__ == '__main__':
    app.run(debug=True)