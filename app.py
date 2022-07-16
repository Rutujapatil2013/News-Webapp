from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=d40bbec766b74174a5adfbec9103e054"
    r = requests.get(url).json()

    cases = {
        'articles' : r['articles']
    }

    return render_template('index.html', case = cases)

if __name__=="__main__":
    app.run(debug=True,port=8000)