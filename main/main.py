"""
Module that creates html page with map with inputed coordinates
and location of filming 10 films of inputed year
"""
import sys
from argparse import ArgumentParser
from check_args import check_args
from get_address import get_addresses_from_file
from get_coords import get_coordinates
from get_distance import get_distance
from create_map import create_map

parser = ArgumentParser(description="Creates map with 10 closest films locations of inputed year")
parser.add_argument("year", type=str,  help="year of films to be shown on map")
parser.add_argument("my_latitude", type=str, help="latitude of your location")
parser.add_argument("my_longitude", type=str,  help="longtitude of your location")
parser.add_argument("path", type=str,  help="path to dataset")
args = parser.parse_args()

def main() -> None:
    """Main function"""
    all_locations = []
    args_validity = check_args(args.year, args.my_latitude, args.my_longitude, args.path)
    if args_validity:
        sys.exit(args_validity)
    my_latt, my_long = float(args.my_latitude), float(args.my_longitude)
    for (film_name,address) in get_addresses_from_file(args.path, args.year):
        if get_coordinates(address):
            (latitude, longitude) = get_coordinates(address)
            distance = get_distance(my_latt, my_long, latitude, longitude)
            all_locations.append((distance, film_name, latitude, longitude))
        if len(all_locations) == 100:
            create_map(all_locations, my_latt, my_long)
            break

if __name__ == "__main__":
    main()
