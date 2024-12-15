# marshmallow 라이브러리
스키마 기반의 데이터 검증 및 직렬화 라이브러리

## 프로젝트 구조
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

