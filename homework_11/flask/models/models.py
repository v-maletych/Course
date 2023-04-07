from app import db


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    body = db.Column(db.Text, nullable=False)


    @property
    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "body": self.body
        }
