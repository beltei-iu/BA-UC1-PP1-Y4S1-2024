from flask import Flask, render_template, request, redirect, url_for, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from os import environ

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://posgres:123456@localhost/posgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def json(self):
        return {'id': self.id,'username': self.username, 'email': self.email}

db.create_all()

@app.route('/')
def hello_world():  # put application's code here
    articles =  [
        1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20
    ]
    return render_template('index.html', articles=articles)

@app.route('/article', methods=['GET', 'POST'])
def article():
    return render_template('article.html')

@app.route('/article-detail', methods=['GET'])
def article_detail():
    return render_template('article_detail.html')


if __name__ == '__main__':
    app.run(debug=True)
