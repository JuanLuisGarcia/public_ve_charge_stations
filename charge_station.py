import requests
import csv

url_all_station = "https://ws.consorcidetransports.com/produccio/ximelib-mobile/rest/devicegroups"

payload = '{"onlyAvailable": false, "includeOffline": true}'
headers = {
    'content-type': "application/json",
    'accept-encoding': "gzip",
    'cache-control': "no-cache",
}

response = requests.request("POST", url_all_station, data=payload, headers=headers)
all_station_json_data = response.json()

out_file = open('vw_ximelib_import.csv', 'w')
writer = csv.writer(out_file)
for value in all_station_json_data:
    url_station_status = f'https://ws.consorcidetransports.com/produccio/ximelib-mobile/rest/devicegroups/{value["id"]}'
    response = requests.request("GET", url_station_status, headers=headers)
    station_status = response.json()
    writer.writerow((value['lng'], value['lat'], station_status['name']))
out_file.close()
print('Done!!')
