from manager import db, dbt, create_app
from manager.lib.JsonDB import JsonDB
import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
app = create_app()

db_uri = JsonDB('DB_uri',path=r"C:\\Users\\LENOVO\\Desktop\\Agustya\\manager")

def drop_all_databses():
    con = psycopg2.connect(dbname='acc_db', user='postgres', host='',password='apku1290')        
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = con.cursor()
    for tenant_name in db_uri.db:
        print(tenant_name)
        cur.execute(sql.SQL(f"DROP DATABASE {tenant_name}"))    
    db_uri.clear()
    db_uri.commit()

with app.app_context():    
    
    db.drop_all()
    dbt.drop_all()    
    
    db.create_all()
    dbt.create_all()

    drop_all_databses()