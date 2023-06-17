from flask import jsonify, render_template, request, Blueprint
from .models import Car

main = Blueprint('main', __name__)
@main.route('/')
def index():
    return render_template('index.html')


@main.route('/search', methods=['POST'])
def search():
    keyword = request.json['keyword']
    results = Car.query.filter(Car.make.like(f'%{keyword}%')).all()
    return jsonify(results=[car.serialize() for car in results])


@main.route('/detail/<int:car_id>')
def detail_view(car_id):
    car  = Car.query.get_or_404(car_id)
    return render_template('detail_view.html', car=car) 