from flask import Flask, request, render_template
from find_distance import calculate_distance, get_road_distance

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index() -> str:
    if request.method == 'POST':
        city_1: str = request.form['city_1'].title()
        city_2: str = request.form['city_2'].title()

        if city_1 == city_2:
            return render_template('index.html', error_message='You entered the same city in both fields.')

        try:
            distance: float = calculate_distance(city_1, city_2)
            road_distance = get_road_distance(city_1, city_2)
            if isinstance(road_distance, float):
                road_distance = f'Distance: {round(road_distance, 2)} km.'

            return render_template(
                'result.html',
                city_1=city_1,
                city_2=city_2,
                distance=round(distance, 2),
                road_distance=road_distance
            )

        except Exception:

            return render_template('index.html',
                                   error_message='An error has occurred, check the correctness of the input.')

    return render_template('index.html', error_message=None)


if __name__ == '__main__':
    app.run(debug=True)
