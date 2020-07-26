from flask import Blueprint, redirect, request, flash, url_for, render_template, current_app
from flask_login import login_required, login_user, current_user, logout_user

from manager.lib.safe_next_url import safe_next_url
from manager.apps.users.decorators import anonymous_required
from manager.models import Users, set_db_for_binders
from manager.apps.users.forms import LoginForm, BeginPasswordResetForm, PasswordResetForm, SignupForm
from manager.apps.users.forms import UpdateCredentials
from manager import db, dbt

users = Blueprint('users', __name__)


@users.route('/login', methods=['GET', 'POST'])
@anonymous_required()
def login():
    form = LoginForm(next=request.args.get('next'))    

    if form.validate_on_submit():
        u = Users.find_by_identity(form.identity.data)
        
        if u and u.authenticated(password=form.password.data):
            is_remembered = request.form.get('remember', False)
            if login_user(u, remember=is_remembered) and u.is_active():
                u.update_activity_tracking(request.remote_addr)
                dbt.choose_tenant(u.username)

                next_url = request.form.get('next')
                if next_url:
                    return redirect(safe_next_url(next_url))

                return redirect(url_for('main.home'))
            else:
                flash('This account has been disabled.', 'danger')
        else:
            flash('Identity or password is incorrect.', 'danger')

    return render_template('apps/main/before_signup/auth/login.html', form=form)


@users.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('users.login'))


@users.route('/account/begin_password_reset', methods=['GET', 'POST'])
@anonymous_required()
def begin_password_reset():
    form = BeginPasswordResetForm()

    if form.validate_on_submit():
        u = Users.initialize_password_reset(request.form.get('identity'))

        flash('An email has been sent to {0}.'.format(u.email), 'success')
        return redirect(url_for('users.login'))

    return render_template('apps/main/before_signup/auth/begin_password_reset.html', form=form)


@users.route('/account/password_reset', methods=['GET', 'POST'])
@anonymous_required()
def password_reset():
    form = PasswordResetForm(reset_token=request.args.get('reset_token'))

    if form.validate_on_submit():
        u = Users.deserialize_token(request.form.get('reset_token'))

        if u is None:
            flash('Your reset token has expired or was tampered with.',
                  'danger')
            return redirect(url_for('users.begin_password_reset'))

        form.populate_obj(u)
        u.password = Users.encrypt_password(request.form.get('password'))
        u.save()

        if login_user(u):
            flash('Your password has been reset.', 'success')
            return redirect(url_for('users.settings'))

    return render_template('apps/main/before_signup/auth/password_reset.html', form=form)


@users.route('/signup', methods=['GET', 'POST'])
@anonymous_required()
def signup():
    form = SignupForm()

    if form.validate_on_submit():
        user = Users(username=form.username.data.lower(),
                     password = form.password.data,
                     email=form.email.data.lower(),
                     phone=form.phone.data
                    )        
        db.session.add(user)
        db.session.commit()
        Users.__table__.create(bind=dbt.engine, checkfirst=True)
        user_dbt = Users(username= user.username,
                        password = user.password,
                        email= user.email,
                        phone= user.phone)
        dbt.session.add(user_dbt)
        dbt.session.commit()

        if login_user(user):            
            dbt.create_db_for_tenant(app=current_app, tenant_name=user.username)            
            dbt.choose_tenant(user.username)            
            flash('Awesome, thanks for signing up!', 'success')
            return redirect(url_for('users.welcome'))

    return render_template('apps/main/before_signup/auth/signup.html', form=form)


@users.route('/welcome', methods=['GET', 'POST'])
@login_required
def welcome():    
    if not len(current_user.companies) == 0:    
        return redirect(url_for('main.home'))
    set_db_for_binders(dbt.engine)
    return render_template('apps/main/after_signup/welcome.html')


@users.route('/settings')
@login_required
def settings():
    return render_template('apps/users/before_signup/settings.html')


@users.route('/settings/update_credentials', methods=['GET', 'POST'])
@login_required
def update_credentials():
    form = UpdateCredentials(current_user, uid=current_user.id)

    if form.validate_on_submit():
        new_password = request.form.get('password', '')
        current_user.email = request.form.get('email')

        if new_password:
            current_user.password = Users.encrypt_password(new_password)

        current_user.save()

        flash('Your sign in settings have been updated.', 'success')
        return redirect(url_for('users.settings'))

    return render_template('apps/users/before_signup/update_credentials.html', form=form)
