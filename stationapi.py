from flask import Flask, jsonify, render_template

from stationdict import stationnamedict

app = Flask(__name__)


@app.route('/')
def apiinfo():
    return render_template('apiinfo.html')


@app.route('/api/<string:stationfullname>')
def findstationshortname(stationfullname):
    stationfullname = stationfullname.upper()
    try:
        return jsonify({"stationname": stationfullname, "stationcode": stationnamedict[stationfullname]})
    except KeyError:
        return jsonify({"error": "notfound"})


if __name__ == '__main__':
    app.run()
