from flask import Blueprint, jsonify, make_response, request, abort

isDebug = True
weather_api = Blueprint("weather_api", __name__)

@weather_api.route("/weather", methods=['GET', 'POST'])
def get_weather():
    data = []
    params = ['imgYear', 'imgMonth', 'imgDay', 'imgHour', 'lon', 'lat']
    try:
        if request.method == 'GET':
            print('GET')
            for param in params:
                data.append(request.args.get(param, ''))

            print(data)

            response = {}
            for d in data:
                response.setdefault('res', 'param is : ' + d)
            return make_response(jsonify(response))
        elif request.method == 'POST':
            print('POST')
            print(request.form['query'])
            return request.form['query']
        else:
            return abort(400)
    except Exception as e:
        return str(e)