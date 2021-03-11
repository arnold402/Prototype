#create endpoints and system logic
from app.admin import blueprint
from flask import jsonify, render_template, redirect, request, url_for, flash
from flask_login import (
    current_user,
    login_required,
    login_user,
    logout_user
)
from sqlalchemy.sql.functions import func
from app import db, login_manager
from app.base.forms import LoginForm
from app.admin.forms import AddUserForm, UpdateUserForm
from app.base.models import User

from app.base.util import verify_pass

@blueprint.route('/dashboard')
def admin_dashboard():
    user_count = db.session.execute(User.query.filter_by().statement.with_only_columns([func.count()]).order_by(None)).scalar()
    users = User.query.all()
    return render_template('dashboard.html', user_count=user_count, users=users)


@blueprint.route('/update_user/<int:user_id>', methods=['GET', 'POST'])
def update_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    form = UpdateUserForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            #Update User
            user.username = form.username.data
            user.email    = form.email.data
            user.role     = form.role.data
            db.session.commit()
            flash('INFO: User account has been updated!', 'success')
            return redirect(url_for('admin_blueprint.update_user'))

    elif request.method == 'GET':
        form.username.data = user.username
        form.email.data = user.email
        form.role.data = user.role
    return render_template('update_user.html', form=form,user = user)


@blueprint.route('/new_user', methods=['GET', 'POST'])
def new_user():
    form = AddUserForm()
    if form.validate_on_submit():
        username = form.username.data
        email    = form.email.data
        role     = form.role.data
        password = form.password.data
        # Check usename exists
        user = User.query.filter_by(username=username).first()
        if user:
            flash('Username already exists.','danger')
            return render_template( 'new-user.html',
                                    form=form)

        # Check email exists
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.','danger')
            return render_template( 'new-user.html',
                                    form=form)

        # else we can create the user
        user = User(
                    username = username,
                    email = email,
                    role = role,
                    password = password
        )
        db.session.add(user)
        db.session.commit()
        flash('User created succefully.','success')
        return render_template( 'new-user.html',
                                form=form)

    else:

        return render_template( 'new-user.html', form=form)
