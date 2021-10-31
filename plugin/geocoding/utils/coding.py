import requests
from .transforms import bd09_to_wgs84


def geo_coding(address, key):
    url = "http://api.map.baidu.com/geocoder/v2/?address=" + address + "&output=json&ak=" + key
    reponse = requests.get(url=url)
    reponse.encoding = "utf-8"
    data = reponse.json()
    try:
        if data["status"] == 0:
            lon, lat = bd09_to_wgs84(
                data["result"]["location"]["lng"], 
                data["result"]["location"]["lat"])
            return {"address": address,
                    "point": "POINT(" + str(lon) + " " + str(lat) + ")",
                    "level": data["result"]["level"]}
    except BaseException as e:
        print(e)