#create db models/tables
from sqlalchemy import Binary, Column, Integer, String

from app import db
from app.base.models import User

class Sales(db.Model):

    __tablename__ = 'Sales'

    id = Column(Integer, primary_key=True)
    cust_fname = db.Column(db.String(255))
    cust_lname = db.Column(db.String(255))
    email = db.Column(db.String(255))
    cust_phone_no = db.Column(db.String(50))
    product_code = db.Column(db.String(10))
    qnt = db.Column(db.String(10))
    warranty_status = db.Column(db.String(10))
    delivery = db.Column(db.String(10))
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)

    def __repr__(self):
        return str(self.cust_fname,self.email)
