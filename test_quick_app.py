import pytest
from flask import url_for
from app import app, db, Product, CartItem


@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:power2024@db:3306/speedymart'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client


def test_index(client):
    response = client.get('/')
    assert response.status_code == 200


def test_add_product(client):
    response = client.post('/add_product', data=dict(
        name='Test Product',
        price=10.0,
        stock=5,
        description='Test Description'
    ), follow_redirects=True)
    assert b'Test Product' in response.data
    assert b'Product added successfully!' in response.data


def test_add_to_cart(client):
    product = Product(name='Test Product', price=10.0, stock=5, description='Test Description')
    db.session.add(product)
    db.session.commit()

    response = client.post('/add_to_cart/1', data=dict(
        quantity=3
    ), follow_redirects=True)
    assert b'Test Product' in response.data
    assert b'Total Price: $30.00' in response.data


def test_cart(client):
    product = Product(name='Test Product', price=10.0, stock=5, description='Test Description')
    db.session.add(product)
    db.session.commit()

    cart_item = CartItem(product_id=1, quantity=2)
    db.session.add(cart_item)
    db.session.commit()

    response = client.get('/cart')
    assert b'Test Product' in response.data
    assert b'Total Price: $20.00' in response.data
