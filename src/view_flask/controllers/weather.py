from flask import Blueprint, jsonify, make_response, request

weather_api = Blueprint("weather_api", __name__)

@weather_api.route("/", methods=['GET'])
def get_weather():
    # URLパラメータ
    params = request.args
    response = {}
    if 'param' in params:
        response.setdefault('res', 'param is : ' + params.get('param'))
    return make_response(jsonify(response))