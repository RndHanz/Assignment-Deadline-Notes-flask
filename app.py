from flask import Flask, render_template, request, redirect

app = Flask(__name__)
tasks = []  # Simpan sementara di memori

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    title = request.form.get('title')
    deadline = request.form.get('deadline')
    if title and deadline:
        tasks.append({'title': title, 'deadline': deadline})
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
