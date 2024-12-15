# core
- Flask 작동구조 
- Flask 기초적 사용법 
## Flask 작동구조 

## Flask 기초적 사용법 
### Flask 애플리케이션 초기화
#### 일반적인 초기화 방법
```python
# app.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == "__main__":
    app.run(debug=True)
```

#### 애플리케이션 팩토리 패턴
```python
# app.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == "__main__":
    app.run(debug=True)
```

```python
# __init__.py

from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    return app
```
## 기본 라우팅과 블루프린트
### 기본 라우팅
```python
# routes.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Home Page!"

```
### 블루프린트
```python
# controller/user_controller.py

from flask import Blueprint

user_bp = Blueprint('user', __name__)

@user_bp.route('/profile')
def profile():
    return "This is the user profile page."
```
```python
# __init__.py

from flask import Flask
from controller.user_controller import user_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    app.register_blueprint(user_bp, url_prefix='/users')

    return app
```