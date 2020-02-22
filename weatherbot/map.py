import folium

from weatherbot.weather import get_weather


def get_coords(city):
    response = get_weather(city)
    coords_list = [response["coord"]['lat'], response["coord"]['lon']]
    return coords_list


def init_map(coords_list):
    m = folium.Map(location=[0, 0], zoom_start=2)
    folium.Marker(coords_list, popup=None).add_to(m)
    return m






