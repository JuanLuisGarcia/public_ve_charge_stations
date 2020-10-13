import requests
import sys

url_all_station = "https://ws.consorcidetransports.com/produccio/ximelib-mobile/rest/devicegroups"

payload = '{"onlyAvailable": false, "includeOffline": true}'
headers = {
    'content-type': "application/json",
    'accept-encoding': "gzip",
    'cache-control': "no-cache",
}

response = requests.request("POST", url_all_station, data=payload, headers=headers)
all_station_json_data = response.json()

stations_dict = {value["id"]: {'lat': value['lat'], 'lng': value['lng']} for value in all_station_json_data}

# when we send request to all charge stations it's so slow
if '-r' not in sys.argv:
    for value in all_station_json_data:
        url_station_status = f'https://ws.consorcidetransports.com/produccio/ximelib-mobile/rest/devicegroups/{value["id"]}'
        response = requests.request("GET", url_station_status, headers=headers)
        station_status = response.json()
        stations_dict[value['id']] = {
            'lat': value['lat'],
            'lng': value['lng'],
            'name': station_status['name']
        }
print(stations_dict)
