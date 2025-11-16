from flask import Flask,request, render_template,redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
@app.route("/login")
try :
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Creates site.db SQLite file
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable warning

    db = SQLAlchemy(app)
    class User(db.Model):
        username = db.Column(db.String(100), unique=True, nullable=False)
        password = db.Column(db.String(100), nullable=False)

        def __repr__(self):
            return f"<User {self.username}>"

    if __name__ == '__main__':
        with app.app_context():
            db.create_all()  # Creates SQLite database and tables defined by models
        app.run(debug=True)
except SQLAlchemyError as e:
    error_msg = str(e.__dict__['orig'])
    print("SQLAlchemy error:", error_msg)
