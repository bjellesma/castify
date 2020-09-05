from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from models.models import setup_db
from flaskr import create_app

app = create_app()
db = setup_db(app)
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
