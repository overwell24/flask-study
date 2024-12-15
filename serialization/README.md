# serialization
Marshmallow 라이브러리를 사용해 Flask 애플리케이션에서 직렬화/역직렬화를 구현

## 프로젝트 구조
- 순환 참조와 임포트 지연 문제를 해결하기 위해 config/extensions.py로 확장 객체를 분리
- DDD의 철학을 반영하여 domains/users/처럼 각 도메인을 독립된 폴더로 분리

```python
flask_schema/
├── flask_schema/           
│   ├── __init__.py         # 앱 초기화
│   ├── config/             # 설정 관련
│   │   ├── __init__.py
│   │   ├── base.py        # 기본 설정
│   │   └── extensions.py  # Flask 확장
│   ├── domains/          
│   │   ├── __init__.py   
│   │   └── users/        # User 도메인
│   │       ├── __init__.py
│   │       ├── models.py  # SQLAlchemy 모델
│   │       └── schemas.py # Marshmallow 스키마
│   └── routes.py          # API 라우트
└── run.py                 # 실행 파일
```
## 코드 설명
### models.py
```python
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)                      # 기본 키
    username = db.Column(db.String(80), unique=True, nullable=False)  # 사용자 이름 (고유, 필수)
    email = db.Column(db.String(120), unique=True, nullable=False)    # 이메일 (고유, 필수)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)      # 생성 일자 (기본값: 현재 시간)
```
### schemas.py
```python
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User          # 직렬화 및 역직렬화 대상 모델
        load_instance = True  # 역직렬화 시 SQLAlchemy 모델 인스턴스로 로드

    # 필수 필드 및 타입 지정
    username = fields.String(required=True)
    email = fields.Email(required=True)

    # 사용자 이름 중복 검증
    @validates('username')
    def validate_username(self, value):
        if User.query.filter_by(username=value).first():
            raise ValidationError('Username already exists')  # 중복된 사용자 이름에 대한 오류

    # 이메일 중복 검증
    @validates('email')
    def validate_email(self, value):
        if User.query.filter_by(email=value).first():
            raise ValidationError('Email already exists')  # 중복된 이메일에 대한 오류
```
### routes.py 
```python
# 스키마 인스턴스 생성
user_schema = UserSchema()        # 단일 사용자용 스키마
users_schema = UserSchema(many=True)  # 다수 사용자용 스키마

# 사용자 생성 (POST)
@main.route('/users', methods=['POST'])
def create_user():
    try:
        # 요청 JSON 데이터를 역직렬화하여 User 인스턴스 생성
        user = user_schema.load(request.json)
        db.session.add(user)       # 데이터베이스에 사용자 추가
        db.session.commit()        # 변경사항 커밋
        # 생성된 사용자 데이터를 직렬화하여 반환
        return jsonify(user_schema.dump(user)), 201
    except ValidationError as err:
        # 역직렬화 시 검증 오류 발생 시 오류 메시지 반환
        return jsonify(err.messages), 400

# 사용자 목록 조회 (GET)
@main.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()       # 모든 사용자 조회
    # 사용자 리스트를 직렬화하여 반환
    return jsonify(users_schema.dump(users))

# 특정 사용자 조회 (GET)
@main.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)  # 사용자 ID로 조회, 없으면 404 오류 반환
    # 조회된 사용자 데이터를 직렬화하여 반환
    return jsonify(user_schema.dump(user))
```
## 테스트 방법
### 사용자 생성 (POST)
```bash
curl -X POST -H "Content-Type: application/json" -d '{"username":"test1","email":"test1@example.com"}' http://127.0.0.1:5000/users
```
### 사용자 목록 조회 (GET)
```bash
curl http://127.0.0.1:5000/users
```
### 특정 사용자 조회 (GET)
```bash
curl http://127.0.0.1:5000/users/1
```

