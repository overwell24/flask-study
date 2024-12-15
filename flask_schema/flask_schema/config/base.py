from pathlib import Path

# 프로젝트 기본 경로 설정
BASE_DIR = Path(__file__).resolve().parent.parent

# 공통 설정
SECRET_KEY = 'my_default_secret_key'
DEBUG = True
ENV = 'development'

# SQLAlchemy 데이터베이스 URI
DATABASE_URI = f'sqlite:///{BASE_DIR}/default.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False