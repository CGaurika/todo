from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

# Temporary storage for todo items. This will be cleared each time the app restarts.
todo_list = []

@app.route('/')
def index():
    return render_template('index.html', todo_list=todo_list)

@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    if task:
        todo_list.append(task)
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    try:
        todo_list.pop(task_id)
    except IndexError:
        pass  # Handle the error when trying to delete a non-existing task.
    return redirect(url_for('index'))

@app.route('/edit/<int:task_id>', methods=['POST'])
def edit(task_id):
    new_task = request.form['new_task']
    if 0 <= task_id < len(todo_list):
        todo_list[task_id] = new_task
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
