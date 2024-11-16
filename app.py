from flask import Flask, render_template
from config import  BOT_KEY

app = Flask(__name__, template_folder='./templates')


@app.route('/')
def payment():  # put application's code here
    return render_template('payment.html')


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port='80')
