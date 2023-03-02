#!/usr/bin/env python3

from flask import Flask, render_template, redirect, request

app = Flask(__name__)

# Define the trivia question and answer
TRIVIA_QUESTION = "What is the largest planet in our solar system?"
TRIVIA_ANSWER = "Jupiter"

# Define the landing page with the trivia form
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", question=TRIVIA_QUESTION)

# Define the route that the form will POST to
@app.route("/check_answer", methods=["POST"])
def check_answer():
    # Get the user's answer from the form data
    user_answer = request.form["answer"]

    # Check if the user's answer is correct
    if user_answer == TRIVIA_ANSWER:
        # Redirect the user to the "correct" page
        return redirect("/correct")
    else:
        # Return the user to the form to try again
        return redirect("/")

# Define the "correct" page
@app.route("/correct", methods=["GET"])
def correct():
    return "<h1>Correct!</h1>"

if __name__ == "__main__":
    app.run(debug=True)
