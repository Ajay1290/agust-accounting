from manager import db 
from manager.lib.util_sqlalchemy import ResourceMixin


class Products(ResourceMixin, db.Model):
    
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String, unique=True, server_default='')
    product_code = db.Column(db.String, server_default='')
    category = db.Column(db.String, server_default='')
    description = db.Column(db.String, server_default='')

    sales_price = db.Column(db.DECIMAL(precision=20, scale=2), server_default='0')
    purchase_price = db.Column(db.DECIMAL(precision=20, scale=2), server_default='0')
    profit = db.Column(db.DECIMAL(precision=20, scale=2), server_default='0')

    unit = db.Column(db.String, server_default='')
    qty = db.Column(db.Integer, server_default='0')
    low_stock_alert = db.Column(db.Integer, server_default='0')


class Services(ResourceMixin, db.Model):
    
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String, unique=True, server_default='')    
    product_code = db.Column(db.String, server_default='')
    category = db.Column(db.String, server_default='')
    description = db.Column(db.String, server_default='')            
    
    sales_price = db.Column(db.DECIMAL(precision=20, scale=2), server_default='0')
    purchase_price = db.Column(db.DECIMAL(precision=20, scale=2), server_default='0')
    profit = db.Column(db.DECIMAL(precision=20, scale=2), server_default='0')
        
    basis = db.Column(db.String, server_default='')
    cycles = db.Column(db.Integer, server_default='0')
