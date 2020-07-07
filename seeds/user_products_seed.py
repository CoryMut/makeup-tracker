from models import db, connect_db, UserProduct
from app import app
import sys
import random

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///makeup3"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
db.create_all()


for i in range(0, 101):
    rand_num = random.randrange(0, 17200)
    up = UserProduct(user_id=1, product_id=rand_num)
    db.session.add(up)
    db.session.commit()