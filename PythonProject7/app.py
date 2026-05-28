from flask import Flask, render_template, request, redirect, url_for, abort
import random

app = Flask(__name__)

# Дані для фільмів
movies = {
    1: {"title": "Інтерстеллар", "desc": "Науково-фантастична драма про космос."},
    2: {"title": "Початок", "desc": "Фільм про сни всередині снів."},
    3: {"title": "Матриця", "desc": "Класика кіберпанку."}
}

# Список для реєстрації
participants = []

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/countries')
def countries():
    return render_template('countries.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/movies')
def movie_list():
    return render_template('movies.html', movies=movies)

@app.route('/movie/<int:id>')
def movie_detail(id):
    movie = movies.get(id)
    if not movie:
        abort(404)
    return render_template('movie.html', movie=movie)

@app.route('/random')
def random_movie():
    return redirect(url_for('movie_detail', id=random.choice(list(movies.keys()))))

@app.route('/event_register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        time = request.form.get('time')
        if name and email and time:
            participants.append({'name': name, 'email': email, 'time': time})
            return redirect(url_for('show_participants'))
    return render_template('register.html')

@app.route('/participants')
def show_participants():
    return render_template('participants.html', participants=participants)

if __name__ == '__main__':
    app.run(debug=True)