from flask import Flask, render_template, request
from Time_project.password_security import total_score, security_rating
from Time_project.password_generate import generate_password
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/verification', methods=['GET', 'POST'])
def verification():
    if request.method == 'POST':
        password = request.form['password']
        score = total_score(password)
        rating = security_rating(password)
        return render_template(
            'Verification.html',
            password=password,
            score=score,
            rating=rating,
        )
    return render_template('Verification.html')

@app.route('/recommend', methods=['GET', 'POST'])
def recommend():
    if request.method == 'POST':
        keyword = request.form.get('keyword')
        length = int(request.form.get('length', 12))
        try:
            password = generate_password(keyword, length)  
            return render_template('Recommend.html', password=password)
        except ValueError as e:
            return render_template('Recommend.html', error=str(e))
    return render_template('Recommend.html')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)  
