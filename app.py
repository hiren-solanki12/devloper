from flask import Flask , render_template
import sys
import os
app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('main.html')
# ,methods=['GET','POST']

@app.rought(/'puzzle')
def hiru():
    return render_template('add outhre.html')
@app.route("/puzzles")
def puzzle():
    return render_template('puzzles.html')

@app.route("/medium")
def medium():
    return render_template('medium.html')


@app.route("/simple")
def simple():
    return render_template('simple.html')@app.route("/puzzles")
def vishal():
    return render_template('puzzles.html')
@app.route("/puzzles")
def kano():
    return render_template('puzzles.html')

@app.route("/hard")
def hard():
    return render_template('hard.html')


@app.route("/aboutme")
def about():
    return render_template('aboutme.html')


if __name__ == '__main__':
    app.run(debug=True)
