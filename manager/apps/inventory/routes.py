from flask import (Blueprint, flash, redirect, request, url_for, render_template, session)
from flask_login import current_user
from manager import db,dbt
from manager.models import Customers, Products, Services, Suppliers
from manager.apps.inventory.forms import NewProductForm, EditProductForm

inventory = Blueprint('inventory', __name__)

@inventory.route('/inventory', methods=['GET','POST'])
def all_inventory():
    inv = dbt.session.query(Products).all()
    form = NewProductForm()
    if form.validate_on_submit():
        createProuct(form, dbt)
        return redirect(url_for('inventory.all_inventory'))
    return render_template('apps/inventory/inventory.html', form=form, inv=inv)



def createProuct(form, db):
    product = Products(     name = form.name.data,
                            product_code = form.product_code.data,
                            category = form.category.data,
                            description = form.description.data,
                            sales_price = form.sales_price.data,
                            purchase_price = form.purchase_price.data,
                            profit = form.profit.data,
                            unit = form.unit.data,
                            qty = form.qty.data,
                            low_stock_alert = form.low_stock_alert.data,
                    )
    db.session.add(product)
    db.session.commit()
