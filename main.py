from flask import Flask, render_template

app = Flask(__name__)
# __name__ contains value of __main__ when executed, but when imported it holds the name of script(main.py).

@app.route("/")
def home():
    return render_template("home.html")
    # flask will look for html documents in templates folder.
# When app route is called(When user visits), the function is executed.

@app.route("/api/v1/<station>/<date>")
def api(station, date):
    temperature = 23
    return {"station": station,
            "date": date,
            "temperature": temperature}


if __name__ == "__main__":
    app.run(debug=True)
