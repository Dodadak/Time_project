from flask import Flask, render_template, request
from Time_project.password_security import total_score, security_rating
from Time_project.password_generate import generate_password
import os

# Flask 인스턴스 생성 시 템플릿 경로 지정
app = Flask(__name__, template_folder=os.path.join(os.getcwd(), 'Time_project/templates'))
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/verification', methods=['GET', 'POST'])
def verification():
    if request.method == 'POST':
        password = request.form['password']
        score = password_security.total_score(password)
        rating = password_security.security_rating(password)
        return render_template('Verification.html', score=score, rating=rating)
    return render_template('Verification.html')

@app.route('/recommend', methods=['GET', 'POST'])
def recommend():
    if request.method == 'POST':
        keyword = request.form['keyword']
        length = int(request.form['length'])
        try:
            password = password_generate.generate_password(keyword, length)
            return render_template('Recommend.html', password=password)
        except ValueError as e:
            return render_template('Recommend.html', error=str(e))
    return render_template('Recommend.html')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
