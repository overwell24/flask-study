from flask import Flask
from blueprints.users.routes import users_bp
from blueprints.products.routes import products_bp


app = Flask(__name__)

# 블루프린트 등록
app.register_blueprint(users_bp, url_prefix='/users')
app.register_blueprint(products_bp, url_prefix='/products')

if __name__ == '__main__':
    app.run(debug=True)