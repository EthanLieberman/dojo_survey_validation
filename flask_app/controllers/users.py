# controller.py
from wsgiref.validate import validator
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_survey', methods=['post'])
def submit_survey():
    print(request.form)
    data = {
        'name': request.form['name'],
        'location': request.form['location'],
        'language': request.form['language'],
        'comment': request.form['comment']
    }

    if not User.validate_user(data):
        return redirect('/')

    User.save(data)
    return redirect('/result')

@app.route('/result')
def posts_page():
    return render_template('posts.html', info=User.get_last())