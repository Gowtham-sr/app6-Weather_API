from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)
# __name__ contains value of __main__ when executed, but when imported it holds the name of script name(main.py).

stations = pd.read_csv("data/stations.txt", skiprows=17)
stations = stations[["STAID", "STANAME                                 "]]

@app.route("/")
def home():
    return render_template("home.html", data=stations.to_html())
    # flask will look for html documents in templates folder.


# When app route is called(When user visits), the function is executed.

@app.route("/api/v1/<station>/<date>")
def api(station, date):
    filename = "data/TG_STAID" + str(station).zfill(6) + ".txt"
    # zfill method adds 0 to the string until the given string meets with 6 letters
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df['    DATE'] == date]["   TG"].squeeze() / 10
    return {"station": station,
            "date": date,
            "temperature": temperature}

@app.route("/api/v1/<station>")
def all_data(station):
    filename = "data/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])
    result = df.to_dict(orient="records")
    return result

@app.route("/api/v1/yearly/<station>/<date>")
def yearly(station, date):
    filename = "data/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20)
    df["    DATE"] = df["    DATE"].astype(str)
    result = df[df['    DATE'].str.startswith(str(date))].to_dict(orient="records")
    return result


if __name__ == "__main__":
    app.run(debug=True)
