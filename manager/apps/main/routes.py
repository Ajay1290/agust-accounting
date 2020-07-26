from flask import (Blueprint, flash, redirect, request, url_for, render_template, session)
from flask_login import current_user
from manager import db,dbt
from manager.models import set_db_for_binders, Customers

main = Blueprint('main', __name__)

@main.route('/')
def home():    
    if current_user.is_authenticated:                
        return render_template('apps/main/after_signup/dashboard.html')
    return render_template('apps/main/before_signup/home.html')


@main.route('/pricing')
def pricing():
    return render_template('apps/main/before_signup/pricing.html')

@main.route('/reset')
def reset():
    db.drop_all()
    dbt.drop_all()
    db.create_all()
    dbt.create_all()
    return 'True'