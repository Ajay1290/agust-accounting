from flask import Blueprint, redirect, request, flash, url_for, render_template
from flask_login import login_required, login_user, current_user, logout_user

from manager.lib.safe_next_url import safe_next_url
# from manager.apps.users.decorators import anonymous_required
# from manager.apps.sales.models import User
# from manager.apps.sales.forms import LoginForm, BeginPasswordResetForm, PasswordResetForm, SignupForm
# from manager.apps.sales.forms import UpdateCredentials

sales = Blueprint('sales', __name__)

@sales.route('/sales')
def all_sales():
    return render_template('apps/sales/sales.html')


@sales.route('/sales/invoices')
def invoices():
    return render_template('apps/sales/invoices.html')


@sales.route('/sales/product-and-services')
def products():
    return render_template('apps/sales/product-and-services.html')