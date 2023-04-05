from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template


app=Flask(__name__)
app.config['SQLALCHEMY DATABASE_URI']='mysql///blog.db'
db=SQLAlchemy(app)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    body = db.Column(db.Text, nullable=False)



with app.app_context():
    db.create_all()



@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404



@app.route("/")
def index():
    return render_template("main/index.html")



@app.route("/all")
def all():
    article = Article.query.all()
    return render_template("main/all.html", articles=article)



@app.route("/article/<int:id>")
def article_details(id):
    article = Article.query.get(id)
    return render_template("main/article_detail.html", article=article)



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
