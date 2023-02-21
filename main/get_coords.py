"""Gets location address and tranforms it into coordinates"""
from typing import Tuple
from geopy.geocoders import Nominatim

def get_coordinates(address: str) -> Tuple[int,int]:
    """
    Transforms address into coordinates
    Args:
        address (str): location address
    Returns:
        Tuple[int,int]: latitude, longitude
    >>> (get_coordinates("Vienna, Austria"))
    (48.2083537, 16.3725042)
    """
    try:
        geolocator = Nominatim(user_agent="task2")
        location = geolocator.geocode(address,timeout=10)
        return location.latitude, location.longitude
    except (TimeoutError, AttributeError) :
        return None

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
