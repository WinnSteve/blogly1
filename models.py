"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE_URL = "https://www.pgconnects.com/digital/wp-content/uploads/sites/12/2015/07/generic-profile-grey-380x380.jpg"


class User(db.Model):
    """Site user."""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.Text, nullable=False, default=DEFAULT_IMAGE_URL)

    @property
    def full_name(self):
        """full name of user"""

        return f"{self.first_name} {self.last_name}"


def connect_db(app):
    """connects db to flask app"""

    db.app = app
    db.init_app(app)
