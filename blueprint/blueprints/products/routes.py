from flask import Blueprint

products_bp = Blueprint('products', __name__)

@products_bp.route('/')
def get_products():
    return 'Products list'