from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Customer management module
class Customer:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

customers = []

@app.route('/customers')
def list_customers():
    return render_template('customers.html', customers=customers)

@app.route('/add_customer', methods=['POST'])
def add_customer():
    name = request.form.get('name')
    phone = request.form.get('phone')
    customers.append(Customer(name, phone))
    flash('Customer added successfully!')
    return redirect(url_for('list_customers'))

# Billing module
class Bill:
    def __init__(self, customer, amount):
        self.customer = customer
        self.amount = amount

bills = []

@app.route('/billing')
def list_bills():
    return render_template('billing.html', bills=bills)

@app.route('/add_bill', methods=['POST'])
def add_bill():
    customer_name = request.form.get('customer')
    amount = request.form.get('amount')
    bills.append(Bill(customer_name, amount))
    flash('Bill added successfully!')
    return redirect(url_for('list_bills'))

# Service management module
services = ['Internet', 'Mobile', 'Landline']

@app.route('/services')
def list_services():
    return render_template('services.html', services=services)

if __name__ == '__main__':
    app.run(debug=True)
