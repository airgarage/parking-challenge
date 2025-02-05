import requests
from datetime import datetime
from typing import List

class ParkingSpot:
    def __init__(self, spot_data: List[str]):
        self.name = spot_data[0]
        self.address = f'{spot_data[1]} {spot_data[2]} {spot_data[3]}'
        self.lat = spot_data[4]
        self.lon = spot_data[4]
        self.base_price = spot_data[7]
        self.walk_score = None
        self.current_price = None

    def _get_time_multiplier(self) -> float:
        """GEt price multiplier based on the current time of day"""
        current_hour = datetime.now().hour
        # please finish logic based on the config file TIME_MULTIPLIERS
        return 1.0

    def _get_popularity_multiplier(self) -> float:
        """Get price multiplier based on the walk score"""
        # please finish logic based on the config file WALK_SCORE_MULTIPLIER
        return self.walk_score / 100

    def calculate_dynamic_price(self) -> float:
        if not self.walk_score:
            return self.base_price
        time_multiplier = self._get_time_multiplier()
        popularity_multiplier = self._get_time_multiplier()

        return self.base_price * time_multiplier * popularity_multiplier

def get_spots(filename: str) -> List[ParkingSpot]:
    with open(filename) as spots_file:
        reader = csv.reader(spots_file)
        spots = [ParkingSpot(row) for row in reader]
    return spots


def main():
    API_KEY = "YOUR_API_KEY"
    spots = get_spots("parking_spots.csv")

    for spot in spots:
        api_url = f"https://api.walkscore.com/score?format=json&address={spot.address}&lat={spot.lat}&lon={spot.lon}&wsapikey={API_KEY}"
        response = requests.get(api_url)
        result = response
        spot.walk_score = result['walkscore']
        spot.calculate_dynamic_price()
        print(f"{spot.name} with a walk score of {spot.walk_score}: base price is ${spot.base_price:.2f} and current_price is ${spot.current_price:.2f}")


if __name__ == "__main__":
    main()