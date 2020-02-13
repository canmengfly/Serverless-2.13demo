from flask import Flask, abort, render_template

app = Flask(__name__,  static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/love')
def love():
    return render_template('love.html')

if __name__ == '__main__':
    app.run()