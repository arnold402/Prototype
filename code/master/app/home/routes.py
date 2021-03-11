#set up endpoints and system logic
from app.home import blueprint
from flask import render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from app import login_manager
from app import db
from app.base.models import User
from app.home.models import Sales
from app.home.forms import AddsalesForm, UpdatesalesForm
from jinja2 import TemplateNotFound

@blueprint.route('/index')
@login_required
def index():

    return render_template('index.html', segment='index')


@blueprint.route("sales/add", methods=['GET', 'POST'])
@login_required
def add_sales():
    form = AddsalesForm()
    if form.validate_on_submit():
        sales = Sales(
                    cust_fname = form.cust_fname.data,
                    cust_lname = form.cust_lname.data,
                    email = form.email.data,
                    cust_phone_no = form.cust_phone_no.data,
                    product_code = form.product_code.data,
                    qnt = form.qnt.data,
                    warranty_status = form.warranty_status.data,
                    delivery = form.delivery.data,
                    author=current_user)
        db.session.add(sales)
        db.session.commit()
        flash('Entry completed successfully!','success')
        return redirect(url_for('home_blueprint.add_sales'))    
    return render_template("add-sales.html", form=form)



@blueprint.route("sales/<int:sales_id>/update", methods=['GET', 'POST'])
@login_required
def update_sales(sales_id):
    sales = Sales.query.get_or_404(sales_id)
    if sales.author != current_user:
        abort(403)
    form = UpdatesalesForm()
    if form.validate_on_submit():
        sales.cust_fname = form.cust_fname.data
        sales.cust_lname = form.cust_lname.data
        sales.email = form.email.data
        sales.cust_phone_no = form.cust_phone_no.data
        sales.product_code = form.product_code.data
        sales.qnt = form.qnt.data
        sales.warranty_status = form.warranty_status.data
        sales.delivery = form.delivery.data
        db.session.commit()
        flash('Entry Updated successfully!','success')
        return redirect(url_for('home_blueprint.sales_dashboard'))
    elif request.method == 'GET':
        form.cust_fname.data = sales.cust_fname
        form.cust_lname.data = sales.cust_lname
        form.email.data = sales.email
        form.cust_phone_no.data = sales.cust_phone_no
        form.product_code.data = sales.product_code
        form.qnt.data = sales.qnt
        form.warranty_status.data = sales.warranty_status
        form.delivery.data = sales.delivery
    return render_template("update-sales.html", form=form)

@blueprint.route("sales/<int:sales_id>/delete", methods=['POST'])
@login_required
def delete_sales(sales_id):
    sales = Sales.query.get_or_404(sales_id)
    if sales.author != current_user:
        abort(403)
    db.session.delete(sales)
    db.session.commit()
    flash('Entry has been deleted!', 'success')
    return redirect(url_for('home_blueprint.sales_dashbord'))


@blueprint.route("/sales-dashboard")
def sales_dashboard():
    data = Sales.query.all()
    return render_template('sales.html',data=data)


@blueprint.route('/<template>')
@login_required
def route_template(template):

    try:

        if not template.endswith( '.html' ):
            template += '.html'

        # Detect the current page
        segment = get_segment( request )

        # Serve the file (if exists) from app/templates/FILE.html
        return render_template( template, segment=segment )

    except TemplateNotFound:
        return render_template('page-404.html'), 404
    
#    except:
#        return render_template('page-500.html'), 500

# Helper - Extract current page name from request 
def get_segment( request ): 

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment    

    except:
        return None  
