from serialization import create_app
from serialization.routes import main

app = create_app()
if __name__ == '__main__':
    app.register_blueprint(main)
    app.run(debug=True)