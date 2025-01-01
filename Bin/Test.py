"""
TEST APP
"""


from flask import Flask, render_template
from questions import question_store

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('your_template.html', question_store=question_store)
