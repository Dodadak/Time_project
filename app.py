from flask import Flask, render_template, request
from Time_project.password_security import total_score, security_rating  # 비밀번호 보안 점수 및 등급 계산 함수
from Time_project.password_generate import generate_password  # 비밀번호 생성 함수

# Flask 애플리케이션 초기화
app = Flask(__name__)

# 기본 라우트: 홈페이지 렌더링
@app.route('/')
def home():
    return render_template('index.html')  # 'index.html' 템플릿을 렌더링하여 반환

# 비밀번호 검증 페이지 라우트
@app.route('/verification', methods=['GET', 'POST'])
def verification():
    if request.method == 'POST':  # POST 요청일 경우
        password = request.form['password']  # 사용자가 입력한 비밀번호 가져오기
        score = total_score(password)  # 비밀번호 점수 계산
        rating = security_rating(password)  # 비밀번호 보안 등급 계산
        return render_template(
            'Verification.html',  # 'Verification.html' 템플릿 렌더링
            password=password,  # 비밀번호 전달
            score=score,  # 점수 전달
            rating=rating,  # 보안 등급 전달
        )
    return render_template('Verification.html')  # GET 요청일 경우 빈 템플릿 렌더링

# 비밀번호 추천 페이지 라우트
@app.route('/recommend', methods=['GET', 'POST'])
def recommend():
    if request.method == 'POST':  # POST 요청일 경우
        keyword = request.form.get('keyword')  # 사용자 입력 키워드 가져오기
        length = int(request.form.get('length', 12))  # 사용자 입력 길이 가져오기 (기본값 12)
        try:
            password = generate_password(keyword, length)  # 키워드와 길이를 기반으로 비밀번호 생성
            return render_template('Recommend.html', password=password)  # 생성된 비밀번호 전달
        except ValueError as e:  # 길이 조건 위반 등의 오류 처리
            return render_template('Recommend.html', error=str(e))  # 오류 메시지 전달
    return render_template('Recommend.html')  # GET 요청일 경우 빈 템플릿 렌더링

# Flask 애플리케이션 실행
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)  # 디버그 모드 활성화, 0.0.0.0에서 실행, 포트 5000
