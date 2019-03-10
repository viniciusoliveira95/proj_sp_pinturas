from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import os

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev_key',
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
            'sqlite:///' + os.path.join(app.instance_path, 'spPintura.sqlite'),
        SQLALCHEMY_TRACK_MODIFICATIONS = False
    )

    admin = Admin(app)
    db.init_app(app)
    migrate.init_app(app, db)

    from admin.Models import AdminModels

    admin.add_views(ModelView(AdminModels.Cliente, db.session))
    admin.add_views(ModelView(AdminModels.Orcamentos, db.session))
    admin.add_views(ModelView(AdminModels.Estoque, db.session))

    return app