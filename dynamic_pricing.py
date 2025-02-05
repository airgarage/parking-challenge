import requests
from datetime import datetime
from typing import List


# This file contains intentional bugs and issues to fix!

class ParkingSpot:
    def __init__(self, spot_data: List[str]):
        """Initialize parking spot from raw CSV data"""
        self.name = spot_data[0]
        self.address = f'{spot_data[1]} {spot_data[2]} {spot_data[3]}'
        self.lat = spot_data[4]
        self.lon = spot_data[4]
        self.base_price = 10.0
        self.walk_score = None
        self.walk_description = None
        self.current_price = None

    def calculate_dynamic_price(self) -> float:
        """Calculate dynamic price based on various factors"""
        if not self.walk_score:
            return self.base_price

        time_multiplier = self._get_time_multiplier()
        popularity_multiplier = self.walk_score / 100

        self.current_price = self.base_price + time_multiplier * popularity_multiplier
        return self.current_price

    def _get_time_multiplier(self) -> float:
        """Get price multiplier based on time of day"""
        current_hour = datetime.now().hour

        if 9 <= current_hour <= 17:  # Business hours
            return 1.5
        elif 17 <= current_hour <= 23:  # Evening
            return 2.0
        else:  # Early morning
            return 1.0


def get_walk_score_api(spot: ParkingSpot, api_key: str) -> str:
    """Generate Walk Score API URL"""
    url_base = "https://api.walkscore.com/score?format=json"
    address_param = "&address=" + spot.address
    lat = "&lat=" + spot.lat
    lon = "&lon=" + spot.lon
    api_key_param = "&wsapikey=" + api_key

    return url_base + address_param + lat + lon + api_key_param


def process_parking_spots(csv_file: str, api_key: str) -> List[ParkingSpot]:
    """Process parking spots and calculate dynamic prices"""
    spots = []

    with open(csv_file) as f:
        reader = csv.reader(f)
        spots = [ParkingSpot(row) for row in reader]

    for spot in spots:
        try:
            api_url = get_walk_score_api(spot, api_key)
            response = requests.get(api_url)
            result = response

            spot.walk_score = result['walkscore']
            spot.walk_description = result['description']
            spot.calculate_dynamic_price()

        except Exception as e:
            print(f"Error processing {spot.name}: {str(e)}")
            continue

    return spots


def main():
    API_KEY = "PROVIDED_API_KEY"
    spots = process_parking_spots("parking_spots.csv", API_KEY)

    for spot in spots:
        print(f"{spot.name}: {spot.current_price}")


if __name__ == "__main__":
    main()
