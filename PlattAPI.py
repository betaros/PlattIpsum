from flask import Flask
from flask_restx import Resource, Api
from PlattIpsum import PlattIpsum

app = Flask(__name__)
api = Api(app)

platt_ipsum = PlattIpsum()


@api.route('/<int:word_count>')
class PlattIpsum(Resource):

    def get(self, word_count):
        text = platt_ipsum.create_text(word_count)
        return text


if __name__ == '__main__':
    app.run(debug=True)