import folium

from weatherbot.weather import get_weather


def get_coords(city):
    coords_list = []
    response = get_weather(city)
    coords = response["coord"]
    coords_list.append(coords['lat'])
    coords_list.append(coords['lon'])
    return coords_list


m = folium.Map(location=[0, 0], zoom_start=2)
folium.Marker(coords_list, popup=None).add_to(m)
coords_list = get_сoords(city)
m