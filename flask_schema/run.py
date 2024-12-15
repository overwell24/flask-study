from flask_schema import create_app
app = create_app()
from flask_schema.routes import main
if __name__ == '__main__':
    app.register_blueprint(main)
    app.run(debug=True)