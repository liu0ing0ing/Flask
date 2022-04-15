from flask import Flask, render_template, request
from secrets1 import api_key
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1> Welcome! </h1>'

@app.route('/name/<nm>')
def hello_name(nm):
    return render_template('name.html', name=nm)

@app.route('/headlines/<nm>')
def story(nm):
    url = 'https://api.nytimes.com/svc/topstories/v2/technology.json?api-key='+api_key
    results = requests.get(url).json()['results']
    top_articles = []
    for i in results[0:5]:
        title = i['title']
        top_articles.append(title)
    return render_template('headlines.html', name=nm, top_articles=top_articles)


if __name__ == '__main__':
    app.run(debug=True)

