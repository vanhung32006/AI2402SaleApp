import cloudinary
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = 'JKGHJHGHJG&*^*&*&^*^*^^FJHGJHOUT&*T^R*^FJHV'
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@localhost/saledb?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config['PAGE_SIZE'] = 8

db = SQLAlchemy(app=app)
login = LoginManager(app=app)

cloudinary.config(cloud_name='i3c1j8ys',api_key='463393967499462',api_secret='VvEuJK0Mxc6yDjBcJlXXU4wu1UM')