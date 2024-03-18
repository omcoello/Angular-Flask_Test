from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import os
import logging
driver = "mysql"
username = os.getenv("MYSQL_USER")
password = os.getenv("MYSQL_PASSWORD")
database = os.getenv("MYSQL_DATABASE")
host = os.getenv("MYSQL_HOST")
port = os.getenv("MYSQL_PORT")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = driver + '://'+username+':'+password+'@'+host + ':' + port +'/'+database
db = SQLAlchemy(app)

class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    account = db.Column(db.String(50))
    city = db.Column(db.String(50))
    state = db.Column(db.String(50))
    location = db.Column(db.String(50))
    balance = db.Column(db.Float)

class AuditLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    action = db.Column(db.String(255))
    timestamp = db.Column(db.DateTime)
    ip_address = db.Column(db.String(50))

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'  # Permite solicitudes desde cualquier origen
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'  # Permite el encabezado Content-Type
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'  # Permite métodos HTTP específicos
    return response

@app.route('/')
def get_profile_view():
    return render_template('index.html')

@app.route('/api/insert_account', methods=['POST'])
def insert_account():
    data = request.json
    new_account = Account(name=data['name'], account=data['account_number'], city=data['city'], location=data['location'], state=data['state'],balance=data['balance'])
    db.session.add(new_account)
    db.session.commit()
    return jsonify({'message': 'Cuenta insertada correctamente'}), 201

@app.route('/api/get_accounts', methods=['GET'])
def get_accounts():
    accounts = Account.query.all()
    accounts_list = []

    for account in accounts:
        account_data = {
            'id': account.id,
            'name': account.name,
            'account_number': account.account,
            'city': account.city,
            'state': account.state,
            'location': account.location,
            'balance': account.balance
        }
        accounts_list.append(account_data)

    return jsonify(accounts_list)

def getFlaskApp():
    return app

if __name__ == "__main__":
    app.run(debug=True)
