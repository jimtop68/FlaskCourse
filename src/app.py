from flask import Flask, render_template
from flask.json import htmlsafe_dump
import json

app=Flask(__name__)

@app.route("/index")
@app.route("/")
def root():
    return render_template("index.html")



if __name__=="__main__":
    app.run(debug=True)

    