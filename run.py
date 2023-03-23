from flask import Flask, render_template, request
from src.video_info import get_info_stream

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():        
    return render_template('home.html')


@app.route('/result', methods=['GET', 'POST'])
def result():
    url = request.form.get('link')
    info = get_info_stream(url)
    
    return render_template('result.html', info=info)


if __name__ == '__main__':
    app.run(debug=True)
