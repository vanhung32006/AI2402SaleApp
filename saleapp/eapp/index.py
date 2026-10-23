from flask import render_template, request

from saleapp.eapp import app, dao


@app.route("/")
def index():
    products = dao.load_product(kw=request.args.get('kw'),cate_id=request.args.get('category_id'))
    return render_template('index.html', products=products)


@app.route('/login')
def login_view():
    return render_template('login.html')


@app.route('/register')
def register_view():
    return render_template('register.html')


@app.context_processor
def common_responses():
    categories = [{
        'id': 1,
        'name': 'Mobile'
    }, {
        'id': 2,
        'name': 'Tablet'
    }, {
        'id': 3,
        'name': 'Laptop'
    }]

    return {
        'categories': categories
    }


if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)
