from flask import Flask
from config import Config
from models import db
from routes import routes

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()  # Cria as tabelas no banco de dados (somente na inicialização)

app.register_blueprint(routes)

if __name__ == '__main__':
    app.run(debug=True)