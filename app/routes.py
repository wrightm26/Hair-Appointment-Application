from app import app
from flask import render_template
from app.form import SignUpForm

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        full_name = form.full_name.data
        usernames = form.username.data
        passwords = form.password.data
        numbers = form.password.data
        email = form.email.data
        return render_template('login.html')

    return render_template('signup.html', form=form)

@app.route('/locservices')
def locservices():
    return render_template('locservices.html')

@app.route('/braidservices')
def braidservices():
    return render_template('braidservices.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

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
