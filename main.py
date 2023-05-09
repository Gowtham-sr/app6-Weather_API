from flask import Flask, render_template

app = Flask("Website")


@app.route("/home")
def home():
    return render_template("tutorial.html")
    # flask will look for html documents in templates folder.
# When app route is called(When user visits), the function is executed.

@app.route("/about/")
def about():
    return render_template("about.html")


app.run(debug=True)
