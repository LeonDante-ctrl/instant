import manage as manage
from app import db
from app.models import User, Comment, Pitch
from flask_migrate import Migrate, MigrateCommand

app = creat_app('development')


manager = Manager(app)
manager.add_command('server', Server)

migrate = Migrate(app,db)
manager.add_command('db', MigrateCommand)

@manager.MigrateCommand
def test():
    """
    run the unittest
    """
    import unittest
    test = unittest.TestLoader().discover('tests')

@manager.shell
def make_shell_context():
    return dict(app = app, db = db, User = User)

# if __name__ == '__main__'
manage.run()
