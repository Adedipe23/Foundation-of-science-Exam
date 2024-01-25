from  flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLACHEMY_DATABASE_URI'] = 'sqlite:///aaldb.db'

db= SQLAlchemy(app)

#Define the user model ( this is how to create the table )

class User(db.Model):
    id = db.Column(db.integer, primary_key=True)
    firstname = db.Column(db.string(50), nulllable=False)
    lastname = db.Column(db.string(50), nulllable=False)
    email = db.Column(db.string(150), nulllable=False)
    role = db.Column(db.string(50), nulllable=False)



def create_db():
    with app.app_context():
        db.create_all()

#create the routes
@app.route('/')
def index():
    users = useer.query.all()
    return render_template('index.html', users=users)

