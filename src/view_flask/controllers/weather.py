import io
from PIL import Image
from flask import Blueprint, jsonify, make_response, request, abort
from flask.wrappers import Response
from modules.meteorological_img import MeteImg, strToDate


isDebug = True
weather_api = Blueprint("weather_api", __name__)

@weather_api.route("/weather", methods=['GET', 'POST'])
def get_weather():
    data = {}
    params = ['imgYear', 'imgMonth', 'imgDay', 'imgHour', 'imgMinute', 'lon', 'lat', 'zoom']
    try:
        if request.method == 'GET':
            print('GET')
            for param in params:
                data.update({
                    param: request.args.get(param, '')
                })

            date_data = strToDate(
                data['imgYear'],
                data['imgMonth'],
                data['imgDay'],
                data['imgHour'],
                data['imgMinute'],
            )
            mimg = MeteImg(
                date_data,
                data['lon'],
                data['lat'],
                data['zoom'],
            )
            img_path = mimg.cloud_create(True)
            print(img_path)
            img = Image.open(img_path, mode='r')

            img_bytes = io.BytesIO()
            img.save(img_bytes, format='PNG')
            img_bytes = img_bytes.getvalue()

            # response = {}
            # for d in data:
            #     response.setdefault('res', 'param is : ' + d)
            response = make_response(img_bytes)
            response.headers.set('Content-Type', 'image/png')
            return response
        elif request.method == 'POST':
            print('POST')
            print(request.form['query'])
            return request.form['query']
        else:
            return abort(400)
    except Exception as e:
        return str(e)