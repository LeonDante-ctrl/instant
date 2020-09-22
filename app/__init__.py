from flask_uploads import Uploadset, configure_uploads, IMAGES
from flask import flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import loginManager
from flask_mail import Mail


login_manager = loginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
mail = Mail()

bootstrap = Bootstrap()

db.init_app(app)
bootstrap = Bootstrap(app)
login_manager.init_app(app)
db.init_app(app)
login_manager.init_app(app)
mail.init_app(app)

registering the main app blueprint
from .main import main as main_blueprint
app.register_blueprint(main_blueprint)
from .auth import auth as auth_blueprint
app.regidter_blueprint(auth_blueprint, url_prefix = '/authenticate')

#configure UploadSet
configure_uploads(app,photos)

return app