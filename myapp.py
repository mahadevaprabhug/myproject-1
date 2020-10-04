import flask
app = flask.Flask("MyApp")
@app.route("/")
def index():
    return "Wel-Come"

if __name__ == '__main__':
    app.run()
