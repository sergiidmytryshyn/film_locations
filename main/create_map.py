"""
Creates map with inputed location and 10 closest 
and 10 furthest locations of films of given year
"""
import folium

def create_map(all_locations: list, my_lat: float, my_long: float) -> None:
    """Creates map and writes it to .html file"""
    mapp = folium.Map(location=[my_lat, my_long],
                     zoom_start=5)
    mapp.add_child(folium.Marker(location=[my_lat, my_long],
                                popup="My location"))
    closest_locations = folium.FeatureGroup(name="10 closest locations")
    furthest_locations = folium.FeatureGroup(name="10 furthest locations")
    all_locations = sorted(all_locations, key=lambda x: x[0])
    for i in range(10):
        closest_locations.add_child(folium.Marker(
            location=[all_locations[i][-2], all_locations[i][-1]],
            popup=all_locations[i][1],
            icon=folium.Icon(color="green")))
        furthest_locations.add_child(folium.Marker(
            location=[all_locations[-i-1][-2], all_locations[-i-1][-1]],
            popup=all_locations[-i-1][1],
            icon=folium.Icon(color="darkred")))
    mapp.add_child(closest_locations)
    mapp.add_child(furthest_locations)
    mapp.add_child(folium.LayerControl())
    mapp.save('Film_locations.html')
