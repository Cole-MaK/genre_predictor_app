from flask import Flask, render_template, request, redirect, url_for
import requests
import json

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/predict', methods=["GET","POST"])
def predict_genre():
    if request == 'GET':
        return render_template('home.html')
    else:
        song_name=request.form.get('song_name')
        artist=request.form.get('artist')
        url = "http://52.53.155.149:80/predict"
        headers = {"Content-Type": "application/json"} 
        data = {}
        data['song_name'] = str(song_name)
        data['artist'] = str(artist)
        # Sending the POST request 
        response = requests.post(url, json=data, headers=headers)
        result = json.loads(response.text)
        prediction = result['prediction']
        return render_template('home.html', result = prediction, song_name = song_name, artist = artist)