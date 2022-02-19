from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:77889911@192.168.3.205/DVIS?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)

db.create_all()

if __name__ == '__main__':
    app.run(debug=True)

# import pymysql

# if __name__ == '__main__':

#     db = pymysql.connect(host='192.168.3.205',
#                          user='root',
#                          passwd='77889911',
#                          database='DVIS')
#     cursor = db.cursor()
#     print(cursor.execute("SELECT VERSION()"), '1')
#     db.close()
