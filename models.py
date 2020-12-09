"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


class User(db.Model):
    """ Users in the blog website """

    __tablename__ = "users"

    id = db.Columns(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    first_name = db.Columns(db.String(50),
                            nullable=False)
    last_name = db.Columns(db.String(50),
                           nullable=False,
                           default='')
    image_url = db.Columns(db.String,
                           nullable=False,
                           default="/static/default_profile.jpg")