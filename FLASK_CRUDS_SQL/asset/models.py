from tokenize import String
from run import db 
from datetime import datetime
#app/asset/models.py

class Freight(db.Model):
    __tablename__='freight'

    id = db.Column(db.Integer, primary_key=True)
    todays_date = db.Column(db.DateTime)
    notes = db.Column(db.String(100))
    revenue = db.Column(db.Float, nullable=False)
    brokerage = db.Column(db.String(100), nullable=False, index=True)
    driver = db.Column(db.String(100))
    commodity = db.Column(db.String(100))
    weight = db.Column(db.Float(100))
    pickup_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    mileage = db.Column(db.Float(100))
    status = db.Column(db.String(50))

    def __init__(self, todays_date, id, notes, revenue, brokerage, driver, commodity, weight, pickup_date, end_date, mileage, status):
            self.id= id
            self.todays_date = todays_date
            self.notes =notes
            self.revenue = revenue
            self.brokerage = brokerage
            self.driver = driver
            self.commodity = commodity
            self.weight = weight
            self.pickup_date = pickup_date 
            self.end_date = end_date
            self.mileage = mileage
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



class Brokerages(db.Model):
    __tablename__='brokerages'

    id = db.Column(db.Integer, primary_key=True)
    brokerage_name =db.Column(db.String(100), nullable=False)

    def __init__(self, brokerage_name):
        self.brokerage_name = brokerage_name

    
    def __repr__(self):
        return self.brokerage_name
