from saleapp.eapp.models import Category, Products
from saleapp.eapp import app


def load_category():
    return Category.query.order_by('id').all()


def load_product(kw =None,cate_id=None,page=1):
    query = Product.query

    if kw:
        query = query.filter(Product.name.contains(kw))

    if cate_id:
        query = query.filter(Product.category_id == cate_id)
    return query.all()
