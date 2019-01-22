from flask import Flask, request, render_template
import requests

app = Flask(__name__)

def bot_framework(msg):
    
    url = "http://localhost:7878/req"
    data = {"query":msg}
    
    response = requests.post(url, data)
    
    if response.status_code == 200:
        return response.json()['res']
    else:
        return "bot.framework.error"

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/query', methods=["POST"])
def query():
    if request.method == 'POST':
        return bot_framework(request.form['msg'])

if __name__ == '__main__':
    app.run(port=80, debug=True)
    