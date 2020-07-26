from datetime import timedelta
import json

class BaseConfig(object):
    DEBUG = False
    TESTING = False    
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:apku1290@localhost:5432/acc_db'
    SQLALCHEMY_BINDS = json.load(open('manager\\DB_uri.json','r'))

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_LEVEL = 'DEBUG'
    SERVER_NAME = 'localhost:5000'
    SECRET_KEY = 'insecurekeyfordev'
    SEED_ADMIN_EMAIL = 'ajay@gmail.com'
    SEED_ADMIN_PASSWORD = 'apku1290'
    REMEMBER_COOKIE_DURATION = timedelta(days=90)

    # Billing.
    STRIPE_SECRET_KEY='pk_test_51Gvl24HI4BytrmOiqSw5uuaEJQbmhxK3NvDaxiWO4cZC2Xf21EZ46pKJeZwZdAA3NYGK4KMeXlmt9v7WL3mVKJi70056DV231O'
    STRIPE_PUBLISHABLE_KEY='sk_test_51Gvl24HI4BytrmOilXIXvSNnSVTrdnlIedrJUxfgKpnm2cvtQGwm4mtIDSNBIT9bVrI3Kihu568KGETTmwNxGNJU00rqKu1FB7'
    STRIPE_API_VERSION = '2020-03-02'
    STRIPE_CURRENCY = 'usd'
    STRIPE_PLANS = {
        '0': {
            'id': 'bronze',
            'name': 'Bronze',
            'amount': 100,
            'currency': STRIPE_CURRENCY,
            'interval': 'month',
            'interval_count': 1,
            'trial_period_days': 14,
            'statement_descriptor': 'SNAKEEYES BRONZE',
            'metadata': {
                'coins': 110
            }
        },
        '1': {
            'id': 'gold',
            'name': 'Gold',
            'amount': 500,
            'currency': STRIPE_CURRENCY,
            'interval': 'month',
            'interval_count': 1,
            'trial_period_days': 14,
            'statement_descriptor': 'SNAKEEYES GOLD',
            'metadata': {
                'coins': 600,
                'recommended': True
            }
        },
        '2': {
            'id': 'platinum',
            'name': 'Platinum',
            'amount': 1000,
            'currency': STRIPE_CURRENCY,
            'interval': 'month',
            'interval_count': 1,
            'trial_period_days': 14,
            'statement_descriptor': 'SNAKEEYES PLATINUM',
            'metadata': {
                'coins': 1500
            }
        }
    }

class DevConfig(BaseConfig):
    DEBUG = True
    TESTING = False

class TestConfig(BaseConfig):
    DEBUG = False
    TESTING = True