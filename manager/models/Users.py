from manager.ext import db

import datetime
from collections import OrderedDict
from hashlib import md5

import pytz
from flask import current_app
from sqlalchemy import or_
from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import UserMixin

from itsdangerous import URLSafeTimedSerializer, TimedJSONWebSignatureSerializer

from manager.lib.util_sqlalchemy import ResourceMixin, AwareDateTime
# from snakeeyes.blueprints.billing.models.credit_card import CreditCard
# from snakeeyes.blueprints.billing.models.subscription import Subscription


class Users(UserMixin, ResourceMixin, db.Model):    

    ROLE = OrderedDict([
        ('member', 'Member'),
        ('admin', 'Admin')
    ])    

    id = db.Column(db.Integer, primary_key=True)
    # Relationships.
    # credit_card = db.relationship(CreditCard, uselist=False, backref='users',
    #                               passive_deletes=True)
    # subscription = db.relationship(Subscription, uselist=False,
    #                                backref='users', passive_deletes=True)
    # invoices = db.relationship(Invoice, backref='users', passive_deletes=True)

    # Authentication.
    role = db.Column(db.Enum(*ROLE, name='role_types', native_enum=False), index=True, nullable=False, server_default='member')
    active = db.Column('is_active', db.Boolean(), nullable=False, server_default='1')
    username = db.Column(db.String(24), unique=True, index=True)
    phone = db.Column(db.String(13))
    email = db.Column(db.String(255), unique=True, nullable=False, server_default='')
    password = db.Column(db.String(128), nullable=False, server_default='')

    # Billing.
    name = db.Column(db.String(128), index=True)
    organization = db.Column(db.String(128))
    payment_id = db.Column(db.String(128), index=True)
    cancelled_subscription_on = db.Column(AwareDateTime())
    previous_plan = db.Column(db.String(128))

    # Activity tracking.
    sign_in_count = db.Column(db.Integer, nullable=False, default=0)
    current_sign_in_on = db.Column(AwareDateTime())
    current_sign_in_ip = db.Column(db.String(45))
    last_sign_in_on = db.Column(AwareDateTime())
    last_sign_in_ip = db.Column(db.String(45))

    # Additional settings.
    locale = db.Column(db.String(5), nullable=False, server_default='en')    

    # RelationShips
    companies = db.relationship('Company', backref='owner', lazy=True)

    def __init__(self, **kwargs):
        # Call Flask-SQLAlchemy's constructor.
        super(Users, self).__init__(**kwargs)
        self.password = Users.encrypt_password(kwargs.get('password', ''))        

    @classmethod
    def find_by_identity(cls, identity):        
        return Users.query.filter(
          (Users.email == identity) | (Users.username == identity)).first()

    @classmethod
    def encrypt_password(cls, plaintext_password):        
        if plaintext_password:
            return generate_password_hash(plaintext_password)

        return None

    @classmethod
    def deserialize_token(cls, token):        
        private_key = TimedJSONWebSignatureSerializer(
            current_app.config['SECRET_KEY'])
        try:
            decoded_payload = private_key.loads(token)

            return Users.find_by_identity(decoded_payload.get('user_email'))
        except Exception:
            return None

    # @classmethod
    # def initialize_password_reset(cls, identity):        
    #     u = Users.find_by_identity(identity)
    #     reset_token = u.serialize_token()

    #     # This prevents circular imports.
    #     # from manager.apps.user.tasks import (deliver_password_reset_email)
    #     # deliver_password_reset_email.delay(u.id, reset_token)

    #     return u

    @classmethod
    def search(cls, query):
        if not query:
            return ''

        search_query = '%{0}%'.format(query)
        search_chain = (Users.email.ilike(search_query),
                        Users.username.ilike(search_query))

        return or_(*search_chain)

    @classmethod
    def is_last_admin(cls, user, new_role, new_active):
        is_changing_roles = user.role == 'admin' and new_role != 'admin'
        is_changing_active = user.active is True and new_active is None

        if is_changing_roles or is_changing_active:
            admin_count = Users.query.filter(Users.role == 'admin').count()
            active_count = Users.query.filter(Users.is_active is True).count()

            if admin_count == 1 or active_count == 1:
                return True

        return False

    # @classmethod
    # def bulk_delete(cls, ids):
    #     delete_count = 0

    #     for id in ids:
    #         user = Users.query.get(id)

    #         if user is None:
    #             continue

    #         if user.payment_id is None:
    #             user.delete()
    #         else:
    #             # subscription = Subscription()
    #             # cancelled = subscription.cancel(user=user)

    #             # If successful, delete it locally.
    #             # if cancelled:
    #             #     user.delete()

    #         delete_count += 1

    #     return delete_count

    def is_active(self):        
        return self.active

    def get_auth_token(self):        
        private_key = current_app.config['SECRET_KEY']

        serializer = URLSafeTimedSerializer(private_key)
        data = [str(self.id), md5(self.password.encode('utf-8')).hexdigest()]

        return serializer.dumps(data)

    def authenticated(self, with_password=True, password=''):        
        if with_password:
            return check_password_hash(self.password, password)

        return True

    def serialize_token(self, expiration=3600):        
        private_key = current_app.config['SECRET_KEY']

        serializer = TimedJSONWebSignatureSerializer(private_key, expiration)
        return serializer.dumps({'user_email': self.email}).decode('utf-8')

    def update_activity_tracking(self, ip_address):        
        self.sign_in_count += 1

        self.last_sign_in_on = self.current_sign_in_on
        self.last_sign_in_ip = self.current_sign_in_ip

        self.current_sign_in_on = datetime.datetime.now(pytz.utc)
        self.current_sign_in_ip = ip_address

        return self.save()


class Company(ResourceMixin, db.Model):    

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(24), unique=True, index=True)

    # Contant Info
    phone = db.Column(db.String(15), server_default='')
    email = db.Column(db.String(255), server_default='')    
    website = db.Column(db.String(255), server_default='')
    
    # Address
    address = db.Column(db.String(300), server_default='')
    pincode = db.Column(db.String(25), server_default='')
    city = db.Column(db.String(255), server_default='')
    state = db.Column(db.String(255), server_default='')
    country = db.Column(db.String(255), server_default='')

    # Tax Info
    gst = db.Column(db.String(15), server_default='')
    pan = db.Column(db.String(10), server_default='')

    # Meta Info
    is_active = db.Column('is_active', db.Boolean(), nullable=False, server_default='1')

    # RelationShips
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),nullable=False)