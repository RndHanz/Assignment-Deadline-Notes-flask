from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)
tasks = []  # Menyimpan tugas aktif
completed_tasks = []  # Menyimpan tugas yang selesai

@app.route('/')
def index():
    now = datetime.now().date()

    # Pindahkan tugas yang lewat deadline ke tugas selesai
    to_move = [task for task in tasks if datetime.strptime(task['deadline'], '%Y-%m-%d').date() < now]
    for task in to_move:
        tasks.remove(task)
        completed_tasks.append(task)

    return render_template('index.html', tasks=tasks, completed_tasks=completed_tasks)

@app.route('/add', methods=['POST'])
def add():
    title = request.form.get('title')
    deadline = request.form.get('deadline')
    if title and deadline:
        tasks.append({'title': title, 'deadline': deadline})
    return redirect('/')

@app.route('/complete/<int:task_id>')
def complete(task_id):
    if 0 <= task_id < len(tasks):
        completed_tasks.append(tasks.pop(task_id))
    return redirect('/')

@app.route('/delete/<int:task_id>')
def delete(task_id):
    if 0 <= task_id < len(completed_tasks):
        completed_tasks.pop(task_id)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
