"""Calculates distance between two locations"""
from haversine import haversine

def get_distance(lat1: float, long1: float, lat2: float, long2: float) -> float:
    """
    Calculates distance with given coordinates
    Args:
        lat1 (float): latitude of 1 location
        long1 (float): longitude of 1 location
        lat2 (float): latitude of 2 location
        long2 (float): longitude of 2 location
    Returns:
        float: distance
    >>> get_distance(49.80455089028477, 24.35924657893551, 48.80988995966758, 2.984207721492035)
    1548.3448514965762
    """
    return haversine((lat1, long1), (lat2, long2))

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
