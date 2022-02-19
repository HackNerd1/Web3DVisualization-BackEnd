import os
from app import create_app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask import g, render_template
from pymysql import install_as_MySQLdb

app = create_app(os.getenv('FlASK_CONFIG') or 'development')
manager = Manager(app)
migrate = Migrate(app, db)
install_as_MySQLdb()


@app.errorhandler(404)
def page_not_found(e):
    return 'resources not found', 404


manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()