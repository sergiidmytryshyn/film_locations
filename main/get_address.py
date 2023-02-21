"""Gets all addresses of films of given year in file"""

def get_addresses_from_file(path: str, year: str) -> list:
    """
    Reads file and returs list with all addresses of given year films
    Args:
        path (str): path to file with data
        year (str): year of film
    Returns:
        list: all addresses
    """
    with open(path, "r", encoding="utf-8") as toread:
        all_adresses = set()
        for line in toread.readlines():
            if f"({year})" in line:
                (film_name, raw_address) = line.split(f"({year})")[:2]
                raw_address = raw_address.split(" - ")[-1]
                raw_address = raw_address.split(")}")[-1]
                raw_address = raw_address.split(", ")
                raw_address[0] = raw_address[0].split(")")[-1]
                raw_address[-1] = raw_address[-1].split("(")[0]
                raw_address = ", ".join(raw_address).strip()
                all_adresses.add((film_name,raw_address))
    return all_adresses
