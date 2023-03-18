import flask

print(dir(flask))

app = flask.Flask(__name__)


@app.route('/')
def blog():
    return flask.render_template("cv_template.html")


app.run()