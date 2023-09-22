import base64
from app import db, login
import os
from flask_login import UserMixin
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash


class Customer(db.Model, UserMixin):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    number = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(70), nullable=False)


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.password = generate_password_hash(kwargs.get('password'))
        db.session.add(self)
        db.session.commit()

    def check_password(self, password_guess):
        return check_password_hash(self.password, password_guess)

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'username': self.username,
            'password': self.password,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'number': self.number,
            'email': self.email
        }

    def get_token(self, expires_in=300):
        now = datetime.utcnow()
        if self.token and self.token_expiration > now + timedelta(minutes=1):
            return self.token
        self.token = base64.b64encode(os.urandom(24)).decode('utf-8')
        self.token_expiration = now + timedelta(seconds=expires_in)
        db.session.commit()
        return self.token

    def revoke_token(self):
        now = datetime.utcnow()
        self.token_expiration = now - timedelta(seconds=1)
        db.session.commit()

@login.user_loader
def get_a_user_by_id(user_id):
    return db.session.get(Customer, user_id)

class Service(db.Model):
    service_id = db.Column(db.Integer, primary_key=True)
    service_title = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String, nullable=False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        db.session.add(self)
        db.session.commit()

    def to_dict(self):
        return {
            'service_id': self.service_id,
            'service_title': self.service_title,
            'price': self.price,
            'description': self.description,
        }


class Guest(db.Model):
    guestcustomer_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    number = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(70), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey("service.service_id"))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        db.session.add(self)
        db.session.commit()

    def to_dict(self):
        return {
            'customer_id': self.customer_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'number': self.number,
            'email': self.email,
            'service_id': self.service_id
        }


class Orders(db.Model):
    order_id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    service_id = db.Column(db.Integer, db.ForeignKey("service.service_id"))
    customer_id = db.Column(db.Integer, db.ForeignKey("customer.user_id"))
    guestcustomer_id = db.Column(db.Integer, db.ForeignKey("guest.guestcustomer_id"))
    guest_info = db.relationship('Guest', backref='guest')
    service_info = db.relationship('Service', backref='service')
    customer_info = db.relationship('Customer', backref='customer')


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        db.session.add(self)
        db.session.commit()

    def to_dict(self):
        return {
            'order_id': self.order_id,
            'date_created': self.date_created,
            'service_id': self.service_id,
            'customer_id': self.customer_id,
            'guestCustomer_id': self.guestcustomer_id,
        }

class Reviews(db.Model):
    review_id = db.Column(db.Integer, primary_key=True)
    review = db.Column(db.String(100), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        db.session.add(self)
        db.session.commit()

    def to_dict(self):
        return {
            'review_id': self.review_id,
            'review': self.review,
            'date_created': self.date_created
        }
