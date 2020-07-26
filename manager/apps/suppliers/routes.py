from flask import (Blueprint, flash, redirect, request, url_for, render_template, session)
from flask_login import current_user
from manager import db,dbt
from manager.models import Suppliers
from manager.apps.suppliers.forms import NewSupplierForm, EditSupplierForm

suppliers = Blueprint('suppliers', __name__)


@suppliers.route('/suppliers', methods=['GET','POST'])
def all_suppliers():
    suppliers = dbt.session.query(Suppliers).all()
    form = NewSupplierForm()
    if form.validate_on_submit():
        create_new_supplier(form, dbt)
        return redirect(url_for('suppliers.all_suppliers'))
    return render_template('apps/suppliers/suppliers.html', form=form, suppliers=suppliers)


@suppliers.route('/suppliers/<supplier_id>', methods=['GET','POST'])
def supplier_info(supplier_id):
    form = EditSupplierForm()
    supplier = dbt.session.query(Suppliers).get_or_404(supplier_id)
    if request.method == 'GET':
        form.name.data = supplier.name,
        form.company.data = supplier.company
        form.display_name.data = supplier.display_name,
        form.supplier_type.data = supplier.supplier_type,
        form.phone.data = supplier.phone,
        form.email.data = supplier.email,
        form.website.data = supplier.website,
        form.address.data = supplier.address,
        form.pincode.data = supplier.pincode,
        form.city.data = supplier.city,
        form.state.data = supplier.state,
        form.country.data = supplier.country,
        form.gst.data = supplier.gst,
        form.pan.data = supplier.pan
    if form.validate_on_submit():
        edit_supplier(form,dbt,supplier_id)
        return redirect(url_for('suppliers.supplier_info', supplier_id=supplier_id))
    return render_template('apps/suppliers/supplier_info.html', supplier=supplier, form=form)


@suppliers.route('/suppliers/<supplier_id>/inactive', methods=['GET','POST'])
def customer_inactive(supplier_id):    
    supplier = dbt.session.query(Suppliers).get_or_404(supplier_id)
    supplier.is_active = False
    dbt.session.commit()
    return redirect(url_for('suppliers.supplier_info', supplier_id=supplier_id))


@suppliers.route('/suppliers/<supplier_id>/active', methods=['GET','POST'])
def customer_active(supplier_id):
    supplier = dbt.session.query(Suppliers).get_or_404(supplier_id)
    supplier.is_active = True
    dbt.session.commit()
    return redirect(url_for('suppliers.supplier_info', supplier_id=supplier_id))


@suppliers.route('/suppliers/<supplier_id>/delete', methods=['GET','POST'])
def customer_delete(supplier_id):    
    supplier = dbt.session.query(Suppliers).get_or_404(supplier_id)
    dbt.session.delete(supplier)
    dbt.session.commit()
    return redirect(url_for('suppliers.supplier_info', supplier_id=supplier_id))


def create_new_supplier(form, db):
    supplier = Suppliers(   name = form.name.data,
                            company = form.company.data,
                            display_name = form.display_name.data,
                            supplier_type = form.supplier_type.data,
                            phone = form.phone.data,
                            email = form.email.data,
                            website = form.website.data,
                            address = form.address.data,
                            pincode = form.pincode.data,
                            city = form.city.data,
                            state = form.state.data,
                            country = form.country.data,
                            gst = form.gst.data,
                            pan = form.pan.data
                        )
    db.session.add(supplier)
    db.session.commit()

    return None


def edit_supplier(form, db, supplier_id):
    supplier = dbt.session.query(Suppliers).get_or_404(supplier_id)
    if form.validate_on_submit():
        form.name.data = supplier.name,
        form.company.data = supplier.company
        form.display_name.data = supplier.display_name,
        form.supplier_type.data = supplier.supplier_type,
        form.phone.data = supplier.phone,
        form.email.data = supplier.email,
        form.website.data = supplier.website,
        form.address.data = supplier.address,
        form.pincode.data = supplier.pincode,
        form.city.data = supplier.city,
        form.state.data = supplier.state,
        form.country.data = supplier.country,
        form.gst.data = supplier.gst,
        form.pan.data = supplier.pan
        db.session.commit()
    
    return None