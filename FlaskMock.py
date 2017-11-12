#coding:utf-8
from flask import Flask,request
#导入全局变量类
from flask import g
# flask中处理json的类
from flask import jsonify
from flask import render_template

app = Flask(__name__)

#g全局变量生命周期只有一个session，不能当做容器写，只能读
@app.before_request
def set_up_data():
    g.data = [
        {'id': 1, 'title': 'task 1', 'desc': 'this is task 1'},
        {'id': 2, 'title': 'task 2', 'desc': 'this is task 2'},
        {'id': 3, 'title': 'task 3', 'desc': 'this is task 3'},
        {'id': 4, 'title': 'task 4', 'desc': 'this is task 4'},
        {'id': 5, 'title': 'task 5', 'desc': 'this is task 5'}
    ]
    g.task_does_not_exist = {"msg": "task does not exist"}

@app.route("/api/tasks")
def get_all_tasks():
    return jsonify(g.data)


@app.route("/api/tasks/<int:task_id>")
def get_task_by_id(task_id):
    task_index=task_id-1
    if task_id>0 and task_id<=len(g.data):
        return jsonify(g.data[task_index])
    else:
        return jsonify(g.task_does_not_exist)


@app.route("/HF1010")
def HF1010():
    bank=request.args.get("bank",None)
    return render_template("example.xml",bank=bank)
    requests.post(URL)

@app.route('/')
def hello_world():

    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
