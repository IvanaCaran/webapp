from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, template_folder="Templates")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db=SQLAlchemy(app)

class Bilder( db.Model):
    id = db.Column(db.Integer, primary_key= True)
    title = db.Column(db.String(100), nullable=True)  # Beispiel: Titel des Bildes
    artist = db.Column(db.String(100), nullable=True) # Bispiel: Künstlername

@app.route("/Epoche")
def start_page():
    return render_template("Epoche.html")

@app.route('/antike_kunst')
def antike_kunst():
    return render_template('EpocheAntikeKunst.html')

if __name__ == "__main__":
    # Create all database tables if they do not exist
    with app.app_context():
        db.create_all()

    app.run(debug=True)

