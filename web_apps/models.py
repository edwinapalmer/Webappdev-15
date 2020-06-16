


from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

migrate = Migrate()

class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    user_id = db.Column(db.String(128))

    def __repr__(self):
        return f"<Tweet {self.text}>"


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    new_tweet_id = db.Column(db.String(128))

    def __repr__(self):
        return f"<User {self.name}>"
    
def parse_records(database_records):...