import requests
import json
import imageio.v3 as imageio
import matplotlib.pyplot as plt
static_image=requests.get("https://api.tomtom.com/map/1/staticimage?layer=basic&style=main&format=png&bbox=12.968894,79.155922:12.972015,79.137974/json?key=ssaUMWtqzVYRoyl19ClRtpcfkaxWpF5L")
response_API=requests.get("https://api.tomtom.com/routing/1/calculateRoute/12.968894,79.155922:12.972015,79.137974/json?key=ssaUMWtqzVYRoyl19ClRtpcfkaxWpF5L")
print(response_API)
print(static_image)
image=imageio.imread(static_image.content)

data=json.loads(response_API.content)
json_formatted_string = json.dumps(data , indent =4)
#print(json_formatted_string)
latitudes = []
longitudes = []
for point in data['routes'][0]['legs'][0]['points']:
    latitudes.append(point['latitude'])
    longitudes.append(point['longitude'])
    plt.figure(figsize=(20,20))# Show the image
plt.imshow(image, extent = (12.968894,79.155922,12.972015,79.137974))
plt.show()
plt.figure(figsize=(20,20))
plt.imshow(image, extent = (12.968894,79.155922,12.972015,79.137974))
plt.scatter(longitudes,latitudes)
plt.show()

print("Latitudes:", latitudes)
print("Longitudes:", longitudes)

plt.scatter(latitudes,longitudes)
plt.title('smallest Route between points ')
plt.show()
plt.close()
        






