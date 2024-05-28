import unittest
from flask_testing import TestCase
from app import app, db
from models import Product, CartItem

class FlaskTestCase(TestCase):

    def setUp(self):
        # Setup a test client
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        #db.init_app(app)
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()
        # self.app = app.test_client()
        # self.app.testing = True

        # Setup the database
        with app.app_context():
            db.create_all()
            # Add some test data
            product1 = Product(name='Test Product 1', price=10.0, stock=100, description='Test Description 1')
            product2 = Product(name='Test Product 2', price=20.0, stock=200, description='Test Description 2')
            db.session.add(product1)
            db.session.add(product2)
            db.session.commit()

    def tearDown(self):
        # Cleanup the database
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_index(self):
        # Test the index route
        with app.test_client() as client:
            response = client.get('/')
        self.assertEqual(response.status_code, 200)
        
    def test_add_to_cart(self):
        # Test adding a product to the cart
        with app.test_client() as client:

            response = client.post('/add_to_cart/1', data=dict(quantity=1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Cart', response.data)

        # Check if the cart item was added
        with app.test_client() as client:
            cart_item = CartItem.query.filter_by(product_id=1).first()
            self.assertIsNotNone(cart_item)
            self.assertEqual(cart_item.quantity, 1)

    def test_cart(self):
        # Test the cart route
        with app.test_client() as client:
            cart_item = CartItem(product_id=1, quantity=2)
            db.session.add(cart_item)
            db.session.commit()

        response = self.app.get('/cart')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Product 1', response.data)
        self.assertIn(b'20.0', response.data)  # 2 * 10.0

    def test_add_product(self):
        # Test the add_product route
        with app.test_client() as client:
            response = client.post('/add_product', data=dict(
                name='New Product',
                price=30.0,
                stock=300,
                description='New Product Description'
            ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Product added successfully!', response.data)

        # Check if the product was added
        with app.test_client() as client:
            product = Product.query.filter_by(name='New Product').first()
            self.assertIsNotNone(product)
            self.assertEqual(product.price, 30.0)
            self.assertEqual(product.stock, 300)
            self.assertEqual(product.description, 'New Product Description')

if __name__ == '__main__':
    unittest.main()
