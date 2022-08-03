from run import db 
from datetime import datetime
#app/asset/models.py

class Transaction(db.Model):
    __tabelname__='transaction'

    id = db.Column(db.Integer, primary_key=True)
    revenue = db.Column(db.Float, nullable=False)
    brokerage = db.Column(db.String(100), nullable=False, index=True)
    driver = db.Column(db.String(100))
    pickup_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    status = db.Column(db.String(50))

    def __init__(self, id, revenue, brokerage, driver, pickup_date, end_date, status):
            self.id= id
            self.revenue = revenue
            self.brokerage = brokerage
            self.driver = driver
            self.pickup_date = pickup_date 
            self.end_date = end_date
            self.status = status


            
    def __repr__(self):
        return '{} by {} for {}'.format(self.id, self.brokerage, self.revenue)

#either change this to brokerage or something class asset 


class Asset(db.Model):
    __tablename__ = 'assets'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(100), nullable=False)
    asset_name = db.Column(db.String(100), nullable=False, index=True)

    def __init__(self, type, asset_name):
        self.type = type
        self.asset_name = asset_name

    def __repr__(self):
        return self.asset_name
