from .Customers import Customers
from .Users import Users, Company
from .Inventory import Products, Services
from .Category import Category
from .Suppliers import Suppliers

def set_db_for_binders(engine):
    Customers.__table__.create(bind=engine, checkfirst=True)
    Products.__table__.create(bind=engine, checkfirst=True)
    Services.__table__.create(bind=engine, checkfirst=True)
    Category.__table__.create(bind=engine, checkfirst=True)
    Suppliers.__table__.create(bind=engine, checkfirst=True)    
    Company.__table__.create(bind=engine, checkfirst=True)    

