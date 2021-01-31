import googlemaps
import requests

MY_API_KEY = "AIzaSyCk5ikq69h3QyDNmubBqudKFhrgzmF0_PI"
URL_FORMAT = "https://maps.googleapis.com/maps/api/staticmap?center={}"\
    "&zoom={}&size={}&format={}{}&maptype=roadmap"\
    "&key={}"


def dl_image(filename, img_format, url):
    file_name = "{}.{}".format(filename, img_format[:3])
    res = requests.get(url)
    if res.status_code == 200:
        with open(file_name, "wb") as f:
            f.write(res.content)
    else:
        print("失敗")


def make_url(lat, lng, zoom, size, img_format, custom_icon):
    location = "{},{}".format(lat, lng)
    size_param = "{}x{}".format(*size)
    if custom_icon is None:
        icon_param = ""
    else:
        icon_param = "&markers=icon:{}|{}".format(custom_icon, location)
    url = URL_FORMAT.format(
        location, zoom, size_param, img_format, icon_param, MY_API_KEY)
    return url


def get_map_image(
        place, zoom, size=(600, 600), img_format="png",
        custom_icon=None, filename=None):
    """
    place : 場所\n
    zoom  : 1)世界 5)大陸 10)市 15)通り 20)建物\n
    size  : (width, height) 最大 640x640\n
    img_format : png(png8), png32, gif, jpg, jpg-baseline\n
    custom_icon : IconのURL
    """
    # gmaps = googlemaps.Client(key=MY_API_KEY)
    # geocode_result = gmaps.geocode(place)
    # for k, v in geocode_result[0].items():
    #     print("key : " + k)
    #     print(v)
    #     print("-" * 10)

    # lat = geocode_result[0]["geometry"]["location"]["lat"]
    # lng = geocode_result[0]["geometry"]["location"]["lng"]
    lat = 33.719770
    lng = 133.525085
    url = make_url(lat, lng, zoom, size, img_format, custom_icon)
    if filename is None:
        filename = place
    dl_image(filename, img_format, url)


if __name__ == "__main__":
    get_map_image(
        "高知", 7, filename="kochi")