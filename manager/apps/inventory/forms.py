from flask_wtf import Form
from flask import request
from wtforms import HiddenField, StringField, PasswordField, BooleanField, TextAreaField, SelectField
from wtforms.fields import IntegerField, DecimalField
from wtforms.validators import DataRequired, Length, Optional, Regexp, EqualTo, ValidationError
from wtforms_components import EmailField, Email
from wtforms_alchemy.validators import Unique
from manager.lib.util_wtforms import ModelForm
from manager.models import Products, Suppliers
from manager.ext import db, dbt
from manager.apps.users.validations import ensure_identity_exists, ensure_existing_password_matches

class NewProductForm(ModelForm):
    # Genral Info
    name = StringField('Name', validators=[DataRequired(),
                                                Unique(Products.name, get_session=lambda: dbt.session)])
    product_code = StringField('Product Code')
    category = StringField('Category')
    description = TextAreaField('Description')
    
    sales_price = DecimalField(places=2,  validators=[Optional()])
    purchase_price = DecimalField(places=2, validators=[Optional()])
    profit = DecimalField(places=2, validators=[Optional()])

    unit =  SelectField(u'Unit',
                            choices=[   ('BAG', 'BAG - BAGS'),
                                        ('BOT', 'BOT - BOTTLES'),
                                        ('BOX', 'BOX - BOXES'),
                                        ('CMS', 'CMS - CENTIMETERS'),                                        
                                        ('CAN', 'CAN - CANS'),
                                        ('DOZ', 'DOZ - DOZENS'),
                                        ('DRUM', 'DRUM - DRUMS'),                                        
                                        ('KGS', 'KGS - KILLOGRAMS'),
                                        ('PCS', 'PCS - PIECES'),
                                        ('PAC', 'PAC - PACKS'),
                                        ('TON', 'TON - TONES'),
                                        ('UNT', 'UNT - UNITS'),                                        
                                        ('YDS', 'YDS - YARDS'),                                        
                                    ]
                        )
    qty = IntegerField("Qty", validators=[Optional()])
    low_stock_alert = IntegerField('Low Stock Alert', validators=[Optional()])
    

class EditProductForm(ModelForm):
    # Genral Info
    name = StringField('Name', validators=[DataRequired()])
    product_code = StringField('Product Code')
    category = StringField('Category')
    description = TextAreaField('Description')
    
    sales_price = DecimalField(places=2)
    purchase_price = DecimalField(places=2)
    profit = DecimalField(places=2)

    unit =  StringField('Unit')
    qty = IntegerField("Qty") 
    low_stock_alert = IntegerField('Low Stock Alert')    

