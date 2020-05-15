from flask import Flask, flash, redirect, render_template, request, session, abort, jsonify, session
import json
from random import randint
from time import time,sleep

app = Flask(__name__)

@app.route("/")
def splash():
    return render_template('splash.html')

@app.route("/playing", methods=['GET','POST'])
def inprogress():

    #initialise number, lower and upper bounds here
    number =
    lower_bound =
    upper_bound = 

    default_value = '0'
    try:
        current_guess = int(request.form.get('text',default_value))
        # inplement your checking code here.

    except:
        guess_message = "Please enter a whole number between " + str(lower_bound) + " and " + str(upper_bound) + "."

    return render_template('playing.html',guess_message=guess_message,upper_bound=upper_bound,lower_bound=lower_bound)

if __name__ == "__main__":
    app.run(debug=True)
