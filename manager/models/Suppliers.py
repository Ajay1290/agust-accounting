from manager.ext import db,dbt
from manager.lib.util_sqlalchemy import ResourceMixin, AwareDateTime

class Suppliers(ResourceMixin, db.Model):        

    id = db.Column(db.Integer, primary_key=True)

    # Genral Info
    name = db.Column(db.String(50), nullable=False)    
    company = db.Column(db.String(50), index=True)
    display_name = db.Column(db.String(50), nullable=False)
    supplier_type = db.Column(db.String(50))

    # Contant Info
    phone = db.Column(db.String(15), server_default='')
    email = db.Column(db.String(255), server_default='')    
    website = db.Column(db.String(255), server_default='')

    # Billing Address
    address = db.Column(db.String(300), server_default='')
    pincode = db.Column(db.String(25), server_default='')
    city = db.Column(db.String(255), index=True, server_default='')
    state = db.Column(db.String(255), server_default='')
    country = db.Column(db.String(255), server_default='')

    # Tax Info
    gst = db.Column(db.String(15), server_default='')
    pan = db.Column(db.String(10), server_default='')

    # Meta Info
    is_active = db.Column('is_active', db.Boolean(), nullable=False, server_default='1')    

