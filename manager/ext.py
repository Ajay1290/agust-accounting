from flask_wtf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask import session
import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from manager.lib.JsonDB import JsonDB

class MultiTenantSQLAlchemy(SQLAlchemy):

    def choose_tenant(self, tenant_name):
        session['tenant'] = tenant_name
        session.modified = True
        super().get_engine(bind=tenant_name)

    def get_engine(self, app=None, bind=None):
        if bind is None:
            try:
                bind = session['tenant']
            except Exception as e:
                print(e)
        return super().get_engine(bind=bind)

    def create_db_for_tenant(self, app=None, tenant_name=None):
        if tenant_name:
            con = psycopg2.connect(dbname='acc_db', user='postgres', host='',password='apku1290')
            con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            cur = con.cursor()
            cur.execute(sql.SQL(f"CREATE DATABASE {tenant_name}"))
            db_uris = JsonDB('DB_uri', path="C:\\Users\\LENOVO\\Desktop\\Agustya\\manager")
            db_uris.add(tenant_name,f'postgresql://postgres:apku1290@localhost:5432/{tenant_name}')
            db_uris.commit()
            binds = app.config['SQLALCHEMY_BINDS']
            binds[tenant_name] = f'postgresql://postgres:apku1290@localhost:5432/{tenant_name}'
            app.config.update(SQLALCHEMY_BINDS = binds)
            return True
        return False


csrf = CSRFProtect()
db = SQLAlchemy()
dbt = MultiTenantSQLAlchemy()
login_manager = LoginManager()