import subprocess

from bokeh.embed import autoload_server
from flask import Flask, render_template

app = Flask(__name__)

bokeh_process = subprocess.Popen(
    ['bokeh', 'serve','--allow-websocket-origin=127.0.0.1:5000','generator.py'], stdout=subprocess.PIPE)


@app.route("/")
def some_path():
    script=autoload_server(model=None,
                           url="http://localhost:5006/generator"
                           )
    return render_template('slide.html',bokS=script)

if __name__ == "__main__":
    app.run()