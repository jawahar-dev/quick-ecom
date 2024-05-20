Usage Guidelines:
-----------------------
install requirements using  "pip install -r requirements.txt"
and create virtual env using  "python -m venv venv"
activate it, "intrestapp/venv/scripts/activate"

then run flask app using, python app.py

hit the server using "given localhost - http://127.0.0.1:5000"

and call these routes  "Add Loan"  "Add Investment" "Add Savings" to add data.
once data added, the schedulers will call every day midnight at 1AM.
the data will show on console.

Adding Financial Products:
-----------------------------------
To add a loan, navigate to the "Add Loan" page and fill out the form with the loan amount and interest rate.
To add an investment, navigate to the "Add Investment" page and fill out the form with the principal amount and interest rate.
To add a savings account, navigate to the   page and fill out the form with the balance and interest rate.

Calculating Interests:
--------------------------
The application automatically calculates interest for loans, investments, and savings accounts based on configurable parameters.
The interest calculation is performed daily and can be accessed through the respective routes: these will be triggered by APscheduler.
/calculate_loan_interest: Calculates interest for loans.
/calculate_investment_interest: Calculates interest for investments.
/calculate_savings_interest: Calculates interest for savings accounts.

Coding Standards and Best Practices:
-----------------------------------------------
The application adheres to the following coding standards and best practices:

PEP 8 compliance for Python code.
Consistent naming conventions for variables, functions, and routes.
Use of Flask SQLAlchemy for database management.
Proper error handling and exception catching.
Unit tests for critical functionality using the unittest framework.