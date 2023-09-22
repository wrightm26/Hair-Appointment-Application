import os
from app import app, db
from flask import render_template, redirect, url_for, flash
from app.forms import ReviewForm
from app.models import Reviews
# from flask_login import login_user, logout_user, login_required

@app.route('/')
def index():
    reviews = Reviews.query.order_by(Reviews.review_id.desc()).all()
    return render_template('index.html', reviews=reviews)

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LogInForm()
#     if form.validate_on_submit():
#         username = form.username.data
#         password = form.password.data
#         print(username, password)
#         customer = Customer.query.filter_by(username=username).first()
#         if customer is not None and customer.check_password(password):
#             login_user(customer)
#             flash(f"You have successfully logged in as @{customer.username}", "success")
#             return redirect(url_for('index'))
#         return render_template('index.html')
#     return render_template('login.html', form=form)

# @app.route('/signup', methods=['GET', 'POST'])
# def signup():
#     form = SignUpForm()
#     if form.validate_on_submit():
#         first_name = form.first_name.data
#         last_name = form.last_name.data
#         username = form.username.data
#         password = form.password.data
#         number = form.number.data
#         email = form.email.data

#         check_user = db.session.execute(db.select(Customer).filter((Customer.username == username) | (Customer.email == email))).scalars().all()

#         if check_user:
#             flash("A user with that username and/or email already exists", "warning")

#             return redirect(url_for("signup"))
#         new_customer = Customer(first_name=first_name, last_name=last_name,  username=username, password=password, number=number, email=email)
#         flash(f"Thank you {new_customer.first_name} {new_customer.last_name} for joining!", "info")
#         return redirect(url_for('login'))
#     return render_template('signup.html', form=form)

# @app.route('/services')
# def services():
#     return render_template('services.html')

# @app.route('/gallery')
# def gallery():
#     return render_template('gallery.html')

# @app.route('/bookit')
# def bookit():
#     return render_template('bookit.html')



@app.route('/review', methods=['GET', 'POST'])
def review():
    form = ReviewForm()
    if form.validate_on_submit():
        review = form.review.data
        db.session.commit()
        review_info = Reviews(review=review)
        flash(f"Thank you for submitting the following review: {review_info.review}", "success")
        return redirect(url_for('index'))
    return render_template('review.html', form=form)

# @app.route('/order/<product_id>/<user_id>', methods=["GET", "POST"])
# @login_required
# def order(product_id, user_id):

#     pull_art = stripe.Product.retrieve(product_id)
#     price_id = pull_art.get("default_price")

#     session = stripe.checkout.Session.create(
#         line_items = [{
#             'price': price_id,
#             'quantity': 1,
#         }],
#         mode = 'payment',
#         success_url = 'http://localhost:5000' + url_for('thankyou', product_id=product_id, user_id=user_id),
#         cancel_url = 'http://localhost:5000' + url_for('cancel')

#     )

#     return redirect(session.url, code=303)
