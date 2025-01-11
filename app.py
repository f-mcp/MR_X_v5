"""
MAIN
"""

import os
from flask import Flask, render_template, request, jsonify
from questions import question_store
from hints import hint_store, required_store, names_store



app = Flask(__name__)

app.config['SECRET_KEY'] = os.urandom(24)  # Use a fixed key for production
app.config['DEBUG'] = True

@app.route('/', methods=['GET', 'POST'])
def home():
    print("oh look we're home")
    if request.method == 'POST':
        name_index = request.form.get('name_index')
        name_answer = request.form.get('answer')

        if name_index in names_store:
            name_data = names_store[name_index]
            correct_answer = name_data[0]  # Use the first item (name) for comparison

            if name_answer.strip().lower() == correct_answer.lower():
                name_data[1] = 2  # Mark as correctly guessed
            else:
                name_data[1] = 1  # Mark as attempted but incorrect

    return render_template('Brief.html', names_store=names_store)




@app.route('/instructions')
def instructions():
    "INSTRUCTIONS FUNCTIONS"
    print("we appear to be rendering the instructions page ")
    return render_template('Instructions.html')  # Create this HTML file



@app.route('/clues', methods=['GET', 'POST'])
def clues():
    "CLUES FUNCTION"
    print("clues func")
    if request.method == 'POST':
        print("1")
        question_index = request.form['question_index']
        user_answer = request.form['answer']

        # Update the state based on the user's answer
        if question_index in question_store:
            print("2")
            question_data = question_store[question_index]
            correct_answer = question_data[1]

            if user_answer.strip().lower() == correct_answer.lower():
                print("a")
                question_data[3] = 2  # Mark as completed
            else:
                print("b")
                question_data[3] = 1  # Mark as attempted

    return render_template('Clue.html', question_store=question_store)



@app.route('/get_hint', methods=['POST'])
def get_hint():
    "HINTS FUNCTION"
    print("hints func")
    question_id = int(request.form['question_id'])
    hint_level = int(request.form['hint_level'])


    # Get the hint (if it actually exists)
    hints = hint_store.get(question_id, [])
    if hint_level < len(hints):
        return jsonify({"hint": hints[hint_level]})


    return jsonify({"hint": None})      # If there are No More Hints



@app.route('/get_required_hint', methods=['POST'])
def get_required_hint():
    """Tells the user which questions they'll need to have previously completed"""
    print("retrieving a hint with get_required_hint")
    question_id = int(request.form['question_id'])

    # Retrieve the required hint
    required_hint = required_store.get(question_id, "No requirements found.")
    return jsonify({"RequiredHint": required_hint})



@app.route('/hints_page')
def hints_page():
    "HINTS PAGE FUNCTION"
    print("and here's some hints")
    return render_template('Hints.html')



@app.route('/submit', methods=['POST'])
def submit_answer():
    "FORM SUBMISSION, IS THIS DEFUNCT? let's test with print()"
    print("HELLOGRELLOHELLOGRELLOHELLOGRELLOHELLOGRELLOHELLOGRELLOHEL")
    name = request.form['name']
    return f"Hello, {name}!"



if __name__ == '__main__':
    app.run(debug=True)
