from flask import Flask, render_template
import telebot
from config import  BOT_KEY

app = Flask(__name__, template_folder='./templates')


@app.route('/payment')
def payment():  # put application's code here
    return render_template('payment.html')

@app.route('/')
def fee():  # put application's code here
    return render_template('fee.html')

@app.route('/finishFee')
def finishfee():  # put application's code here
    return render_template('finishFee.html')

@app.route('/finishFinishFee')
def finishfinishfee():  # put application's code here
    return render_template('finishFinishFee.html')

@app.route('/finish')
def finishpayment():  # put application's code here
    return render_template('finishPayment.html')


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port='80')
