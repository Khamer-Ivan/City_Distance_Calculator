from flask import Flask, request, render_template
from find_distance import calculate_distance, get_road_distance

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index() -> str:
    if request.method == 'POST':
        city_1: str = request.form['city_1'].lower()
        city_2: str = request.form['city_2'].lower()

        if city_1 == city_2:
            return render_template('index.html', error_message='Вы ввели один и тот же город в оба поля.')

        try:
            distance: float = calculate_distance(city_1, city_2)
            road_distance = get_road_distance(city_1, city_2)
            if isinstance(road_distance, float):
                road_distance = f'Расстояние: {round(road_distance, 2)} км.'

            return render_template(
                'result.html',
                city_1=city_1,
                city_2=city_2,
                distance=round(distance, 2),
                road_distance=road_distance
            )

        except Exception:

            return render_template('index.html', error_message='Возникла ошибка, проверьте правильность ввода.')

    return render_template('index.html', error_message=None)


if __name__ == '__main__':
    app.run(debug=True)
