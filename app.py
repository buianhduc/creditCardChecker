from flask import Flask, redirect, render_template, request
import cardChecker
# import cardChecker
app = Flask(__name__,template_folder='template',static_folder='static')

@app.route('/', methods = ["GET","POST"])
def index():
    if request.method == "GET":
        return render_template('index.html')
    elif request.method == "POST":
        cardNumInput = request.form #get user input
        isCreditCardNumberReal = cardChecker.LuhnAlgorithm(cardNumInput['userInput'])
        return render_template('index.html',result = isCreditCardNumberReal)

app.run(debug=True)