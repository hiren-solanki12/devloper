from flask import Flask , render_template
app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('main.html')
# ,methods=['GET','POST']


@app.route("/puzzles")
def puzzle():
    return render_template('puzzles.html')

@app.route("/medium")
def medium():
    return render_template('medium.html')


@app.route("/simple")
def simple():
    return render_template('simple.html')


@app.route("/hard")
def hard():
    return render_template('hard.html')


@app.route("/aboutme")
def about():
    return render_template('aboutme.html')


if __name__ == '__main__':
    app.run(debug=True)
