import flask
app = flask.Flask("MyApp")
@app.route("/")
def index():
    return "Welcome"

if __name__ == '__main__':
    app.run()
