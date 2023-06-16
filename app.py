from flask import Flask, render_template, request, jsonify, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    make = db.Column(db.String(50))
    model = db.Column(db.String(50))
    price = db.Column(db.String(50))

    def serialize(self):
        return {
            'id': self.id,
            'make': self.make,
            'model': self.model,
            'price': self.price,
            'url': url_for('detail_view', car_id=self.id)
        }


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    keyword = request.json['keyword']
    results = Car.query.filter(Car.make.like(f'%{keyword}%')).all()
    return jsonify(results=[car.serialize() for car in results])


@app.route('/detail/<int:car_id>')
def detail_view(car_id):
    car  = Car.query.get_or_404(car_id)
    return render_template('detail_view.html', car=car) 


if __name__ == '__main__':
    app.run(debug=True)
