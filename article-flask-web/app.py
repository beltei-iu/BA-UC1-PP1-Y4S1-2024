from crypt import methods

from flask import Flask, render_template

app = Flask(__name__)

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
    app.run()
