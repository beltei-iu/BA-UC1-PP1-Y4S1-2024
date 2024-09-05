from flask import Flask, render_template

from data_service import mySum

app = Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here

    articles =  [
        mySum(1,2), mySum(2,3), mySum(3,4), mySum(4,5),
    ]

    return render_template('index.html', articles=articles)


if __name__ == '__main__':
    app.run()
