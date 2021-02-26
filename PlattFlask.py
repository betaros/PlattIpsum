from flask import Flask, render_template
from PlattIpsum import PlattIpsum

app = Flask(__name__)


@app.route('/')
def index():
    platt_ipsum = PlattIpsum(100)
    return render_template('PlattFlask.html', text=platt_ipsum.create_text())


@app.route('/<word_count>')
def index_count(word_count=100):
    platt_ipsum = PlattIpsum(int(word_count))
    return render_template('PlattFlask.html', text=platt_ipsum.create_text())


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)
