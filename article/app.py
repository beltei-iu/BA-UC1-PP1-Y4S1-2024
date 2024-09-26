import time
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Correct PostgreSQL URI configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Article(db.Model):
    __tablename__ = 'article'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    body = db.Column(db.String(120), unique=True, nullable=False)

    # def json(self):
    #     return {'title': self.title, 'body': self.body}

with app.app_context():
    # db.drop_all()
    db.create_all()

@app.route('/article', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        print(request.form.get('title'))
        title = str(request.form.get('title'))
        body = str(request.form.get('content'))
        print(title)
        print(body)
        article = Article(id = time.time(), title=title, body=body)
        db.session.add(article)
        db.session.commit()
        return redirect("/home")
    else:
        return render_template('article.html')

@app.route( '/home')
def index():
    articles = Article.query.all()
    return render_template('index.html',articles=articles)

if __name__ == '__main__':
    app.run(debug=True)