from flask import Flask
from html_generator import get_template


app = Flask(__name__)

@app.route('/')
def hello_bokeh():
   return get_template()

app.run(port=5050)