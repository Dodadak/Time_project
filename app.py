from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/verification')
def verification():
    return render_template('Verification.html')

@app.route('/recommend')
def recommend():
    return render_template('Recommend.html')

if __name__ == '__main__':
    app.run(debug=True)

