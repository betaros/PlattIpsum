from flask import Flask, render_template, request, url_for
from PlattIpsum import PlattIpsum

app = Flask(__name__)
platt_ipsum = PlattIpsum()


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        if request.form["textInput"].isnumeric():
            word_count = int(request.form["textInput"])
            if word_count > 100000:
                word_count = 100000
        else:
            word_count = 100
        return render_template('PlattFlask.html', text=platt_ipsum.create_text(int(word_count)), word_count=word_count)
    else:
        return render_template('PlattFlask.html', text=platt_ipsum.create_text(100), word_count=100)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)
