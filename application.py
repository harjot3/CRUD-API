from flask import Flask
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://data.db'

class Book(db.Book):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(120))
    publishor = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.id} - {selfl.book_name}"

@app.route('/')

def index():
    return 'Hello'

@app.route('/Book')
def get_books():
    return {"id":}
