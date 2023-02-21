"""Checks if inpuuted arguments are valid"""
from os import path

def check_args(year: str, lat: str, long: str, path_: str) -> str:
    """
    Checks inputed year, latitude, longtitude and path
    Args:
        year (str): year of film
        lat (str): inputed latitude 
        long (str): inputed longitude
        path_ (str): path to file with data
    Returns:
        str: 
    >>> check_args("2004", "23.334", "45.6666", "aoaoao")
    'Wrong path'
    """
    if not path.isfile(path_):
        return "Wrong path"
    try:
        if not(-90 <= float(lat) <= 90 and -180 <= float(long) <= 180):
            return "Wrong coordinates"
        int(year)
    except ValueError:
        return "Wrong coordinates or year"

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
