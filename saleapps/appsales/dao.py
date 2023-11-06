from app.models import Category, Product
def get_categories():
    return Category.query.all ()
def get_products():
    products = Product.query

    return products.all()