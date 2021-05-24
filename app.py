import os
from flask import Flask, render_template, abort, url_for, json, jsonify
import json
import html
import requests
import subprocess


url = "http://122.166.167.113:8085/emp"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)




app = Flask(__name__)

# read file


@app.route("/")
def index():
    result = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE)
    list = (response.text)
    print(result.stdout)
  
# Using for loop
    for i in list:
        print(i)
    return render_template('index.html', title="page", jsonfile=(result.stdout))

app.run(host='localhost', debug=True)