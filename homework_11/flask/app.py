from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@db:3306/vnv_blog"

db = SQLAlchemy(app)

with app.app_context():
    from routes.main.routes import *
    from models import Article

    db.create_all()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
