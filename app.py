from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECERET_KEY'] = 'secret'


debug = DebugToolbarExtension(app)

@app.route("/")
def questions_form():
    
    prompts = story.prompts

    return render_template('questions.html', prompts=prompts) 

@app.route("/story")
def display_story():

    text = story.generate(request.args)

    return render_template('story.html', text=text)