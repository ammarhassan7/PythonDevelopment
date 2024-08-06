from flask import Flask, request, render_template
import pyshorteners

app = Flask(__name__)

shortener = pyshorteners.Shortener()

@app.route('/', methods=['GET', 'POST'])
def index():
    short_url = ''
    if request.method == 'POST':
        long_url = request.form['url']
        short_url = shortener.tinyurl.short(long_url)
    
    return render_template('index.html', short_url=short_url)

if __name__ == '__main__':
    app.run(debug=True)
