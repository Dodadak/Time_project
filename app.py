from flask import Flask, render_template, request
from Time_project.password_security import total_score, security_rating  # 비밀번호 보안 점수 관련 임포트
from Time_project.password_generate import generate_password  # 비밀번호 생성 관련 임포트

app = Flask(__name__)

# 홈 페이지 라우팅
@app.route('/')
def home():
    return render_template('index.html')

# 비밀번호 보안 점수 확인 페이지 라우팅
@app.route('/verification', methods=['GET', 'POST'])
def verification():
    if request.method == 'POST':
        # 폼에서 받은 비밀번호
        password = request.form['password']
        
        # 보안 점수와 등급 계산
        score = total_score(password)
        rating = security_rating(password)
        
        # 결과를 페이지에 전달하여 렌더링
        return render_template(
            'Verification.html',
            password=password,
            score=score,
            rating=rating,
        )
    return render_template('Verification.html')

# 비밀번호 추천 페이지 라우팅
@app.route('/recommend', methods=['GET', 'POST'])
def recommend():
    if request.method == 'POST':
        # 폼에서 받은 키워드와 길이
        keyword = request.form.get('keyword')
        length = int(request.form.get('length', 12))  # 기본 길이는 12

        try:
            # 비밀번호 생성
            password = generate_password(keyword, length)
            return render_template('Recommend.html', password=password)
        except ValueError as e:
            # 오류 발생 시 오류 메시지 전달
            return render_template('Recommend.html', error=str(e))
    
    return render_template('Recommend.html')

# 애플리케이션 실행
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
