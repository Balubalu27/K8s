from flask import Flask, jsonify

import datetime

app = Flask(__name__)


@app.route('/date')
def index():
    date_now = datetime.date.today().strftime('%m/%d/%Y')
    return jsonify(date=date_now)


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080)
