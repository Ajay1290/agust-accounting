from flask_wtf import Form
from flask import request
from wtforms import HiddenField, StringField, PasswordField, BooleanField, TextAreaField, SelectField
from wtforms.fields import IntegerField, DecimalField
from wtforms.validators import DataRequired, Length, Optional, Regexp, EqualTo, ValidationError
from wtforms_components import EmailField, Email
from wtforms_alchemy.validators import Unique
from manager.lib.util_wtforms import ModelForm
from manager.models import Suppliers
from manager.ext import db, dbt

def edit_lvl_gst_uniquness(form, field):    
    supplier_id = request.path.lstrip('/inventory/suppliers/').rstrip('/edit')
    supplier = dbt.session.query(Suppliers).get_or_404(supplier_id)
    if field.data != supplier.gst:
        if Suppliers.query.filter(Suppliers.gst == field.data).first():
            raise ValidationError(f'Enter Unique GST No.')


class NewSupplierForm(ModelForm):
    # Genral Info
    name = StringField('Name',validators=[DataRequired()])    
    company = StringField('Company')
    display_name = StringField('Display Name',validators=[DataRequired(),
                                                Unique(Suppliers.display_name, get_session=lambda: db.session)])
    supplier_type = SelectField(u'Supplier Type',
                            choices=[('Consumer', 'Consumer'), ('GST Registered', 'GST Registered'), ('GST Unregistered', 'GST Unregistered')])

    # Contant Info
    phone = StringField('Phone', validators=[Optional() ,Length(6, 13)])
    email = EmailField('Email', validators=[Optional(), Email()])
    website = StringField('Website')

    # Billing Address
    address = TextAreaField('Billing Address')
    pincode = StringField('Billing Pincode')
    city = StringField('Billing City')
    state = StringField('Billing State')
    country = StringField('Billing Country')


    # Tax Info
    gst = StringField('GST No.', validators=[Optional(), Unique(Suppliers.gst, get_session=lambda: db.session), Regexp(r'\d{2}[A-Z]{5}\d{4}[A-Z]{1}[A-Z\d]{1}[Z]{1}[A-Z\d]{1}')])
    pan = StringField('PAN No.', validators=[Optional(), Unique(Suppliers.pan, get_session=lambda: db.session), Regexp(r'^[a-zA-Z]{5}[0-9]{4}[a-zA-Z]$')])



class EditSupplierForm(ModelForm):
    # Genral Info
    name = StringField('Name',validators=[DataRequired()])    
    company = StringField('Company')
    display_name = StringField('Display Name',validators=[DataRequired(),
                                                Unique(Suppliers.display_name, get_session=lambda: db.session)])
    supplier_type = SelectField(u'Supplier Type',
                            choices=[('Consumer', 'Consumer'), ('GST Registered', 'GST Registered'), ('GST Unregistered', 'GST Unregistered')])

    # Contant Info
    phone = StringField('Phone', validators=[Optional() ,Length(6, 13)])
    email = EmailField('Email', validators=[Optional(), Email()])
    website = StringField('Website')

    # Billing Address
    address = TextAreaField('Billing Address')
    pincode = StringField('Billing Pincode')
    city = StringField('Billing City')
    state = StringField('Billing State')
    country = StringField('Billing Country')


    # Tax Info
    gst = StringField('GST No.', validators=[Optional(), Unique(Suppliers.gst, get_session=lambda: db.session), Regexp(r'\d{2}[A-Z]{5}\d{4}[A-Z]{1}[A-Z\d]{1}[Z]{1}[A-Z\d]{1}')])
    pan = StringField('PAN No.', validators=[Optional(), Unique(Suppliers.pan, get_session=lambda: db.session), Regexp(r'^[a-zA-Z]{5}[0-9]{4}[a-zA-Z]$')])