from flask import Flask
from flask import request, render_template, redirect

app = Flask(__name__)

global current_text

class Content():

    def __init__(self):
        self.current_text = 'default'
        self.current_image = False
        self.current_link = False

content = Content()

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/", methods=['POST'])
def read_form():
    content.current_text = request.form['text']
    content.current_link = request.form['url']
    return render_template('index.html')

@app.route("/display", methods=['GET'])
def display():
    if content.current_text:
        return render_template('display.html', text = content.current_text)
    elif content.current_image:
        return render_template('display.html', text = content.current_text)
    elif content.current_link:
        return redirect(content.current_link)
