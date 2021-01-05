from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def ladder():
    ladder = [
        {'rank': 1, 'user': 123123123, 'success': 345},
        {'rank': 2, 'user': 9873123123, 'success': 235},
        {'rank': 3, 'user': 125675423123, 'success': 34},
        {'rank': 4, 'user': 5553123123, 'success': 3},
    ]
    return render_template('ladder.html', ladder=ladder)