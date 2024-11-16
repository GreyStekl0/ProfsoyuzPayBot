from flask import Flask, render_template
from config import  BOT_KEY

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('payment.html')


if __name__ == '__main__':
    app.run()
