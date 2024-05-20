import unittest
from app import app, db
from models import Loan, Investment, SavingsAccount

class TestInterestCalculationRoutes(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:power2024@localhost/intrestDB'
        #db.init_app(app)
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_calculate_loan_interest_route(self):
        # Add test data for loans
        loan1 = Loan(amount=1000, interest_rate=5)
        loan2 = Loan(amount=2000, interest_rate=7)
        db.session.add(loan1)
        db.session.add(loan2)
        db.session.commit()

        # Call the route for calculating loan interest
        with app.test_client() as client:
            response = client.get('/calculate_loan_interest')

        # Assert the response
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Total interest on loans:", response.data)

    def test_calculate_investment_interest_route(self):
        # Add test data for investments
        investment1 = Investment(principal=1000, interest_rate=5)
        investment2 = Investment(principal=2000, interest_rate=7)
        db.session.add(investment1)
        db.session.add(investment2)
        db.session.commit()

        # Call the route for calculating investment interest
        with app.test_client() as client:
            response = client.get('/calculate_investment_interest')

        # Assert the response
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Total interest on investments:", response.data)

    def test_calculate_savings_interest_route(self):
        # Add test data for savings accounts
        savings1 = SavingsAccount(balance=5000, interest_rate=3)
        savings2 = SavingsAccount(balance=8000, interest_rate=4)
        db.session.add(savings1)
        db.session.add(savings2)
        db.session.commit()

        # Call the route for calculating savings interest
        with app.test_client() as client:
            response = client.get('/calculate_savings_interest')

        # Assert the response
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Total interest on savings accounts:", response.data)

if __name__ == '__main__':
    unittest.main()
