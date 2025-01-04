"""
MAIN
"""

import os
from flask import Flask, render_template, request, jsonify
from questions import question_store
from hints import hint_store, required_store



app = Flask(__name__)

app.config['SECRET_KEY'] = os.urandom(24)  # Use a fixed key for production
app.config['DEBUG'] = False

@app.route('/')
def home():
    "HOME FUNCTION"
    condition = True  # Change this to True/False to test rendering
    return render_template('Brief.html', condition=condition)  # The main page with your HTML



@app.route('/instructions')
def instructions():
    "INSTRUCTIONS FUNCTIONS"
    return render_template('Instructions.html')  # Create this HTML file



@app.route('/clues', methods=['GET', 'POST'])
def clues():
    "CLUES FUNCTION"
    if request.method == 'POST':
        question_index = request.form['question_index']
        user_answer = request.form['answer']#

        # Update the state based on the user's answer
        if question_index in question_store:
            question_data = question_store[question_index]
            correct_answer = question_data[1]

            if user_answer.strip().lower() == correct_answer.lower():
                question_data[3] = 2  # Mark as completed
            else:
                question_data[3] = 1  # Mark as attempted

    return render_template('Clue.html', question_store=question_store)



@app.route('/get_hint', methods=['POST'])
def get_hint():
    "HINTS FUNCTION"
    question_id = int(request.form['question_id'])
    hint_level = int(request.form['hint_level'])


    # Get the hint (if it actually exists)
    hints = hint_store.get(question_id, [])
    if hint_level < len(hints):
        return jsonify({"hint": hints[hint_level]})


    return jsonify({"hint": None})      # If there are No More Hints



@app.route('/get_required_hint', methods=['POST'])
def get_required_hint():
    """GET REQUIRED HINT FUNCTION"""
    question_id = int(request.form['question_id'])

    # Retrieve the required hint
    required_hint = required_store.get(question_id, "No requirements found.")
    return jsonify({"RequiredHint": required_hint})



@app.route('/hints_page')
def hints_page():
    "HINTS PAGE FUNCTION"
    return render_template('Hints.html')



@app.route('/submit', methods=['POST'])
def submit_answer():
    "FORM SUBMISSION, IS THIS DEFUNCT?"
    name = request.form['name']
    return f"Hello, {name}!"



if __name__ == '__main__':
    app.run()
