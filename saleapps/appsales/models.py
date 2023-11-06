from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from saleapps.appsales import db, app



class Category(db.Model):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    products = relationship('Product', backref='category', lazy=True)

class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    price = Column(Float, default=0)
    image = Column(String(100), default='https://res.cloudinary.com/grover/image/upload/f_webp,q_auto/b_white,c_pad,dpr_2.0,h_500,w_520/f_auto,q_auto/v1632241420/tcv0cs8qg7mkzuerdljr.png')
    active = Column(Boolean, default=True)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)
if __name__ == '__main__':
    with app.app_context():
        # db.create_all()
        # c1 = Category(name='Mobile')
        # c2 = Category(name='Tablet')
        # c3 = Category(name='Desktop')
        # db.session.add(c1)
        # db.session.add(c2)
        # db.session.add(c3)
        # db.session.commit()
        p1= Product(name='iPhone 13', price=22000000, category_id=1)
        p2 = Product(name='Galaxy S23', price=12000000, category_id=2)
        p3 = Product(name='iPad Pro', price=18000000, category_id=2)
        p4 = Product(name='Macbook M1', price=2000000, category_id=1)
        p5 = Product(name='iPhone 12', price=9000000, category_id=1)
        db.session.add_all([p1,p2,p3,p4,p5])
        db.session.commit()
