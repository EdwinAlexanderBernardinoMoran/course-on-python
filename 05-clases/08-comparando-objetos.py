class Coords:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def __eq__(self, other):
        return self.latitude == other.latitude and self.longitude == other.longitude

    # def __ne__(self, other):
    #     return self.latitude != other.latitude or self.longitude != other.longitude

    def __lt__(self, other):
        return self.latitude + self.longitude < other.latitude + other.longitude
    
    def __le__(self, other):
        return self.latitude + self.longitude <= other.latitude + other.longitude

coords = Coords(45.7128, -74.0060)
print(f"Coordinates: {coords.latitude}, {coords.longitude}")  # Output: Coordinates: 44.7128, -74.0060

coordsTwo = Coords(45.7128, -74.0060)
print(f"Coordinates: {coordsTwo.latitude}, {coordsTwo.longitude}")  # Output: Coordinates: 45.7128, -74.0060

print(coords == coordsTwo)  # Output: False
print(coords != coordsTwo)  # Output: True
print(coords > coordsTwo)  # Output: False
print(coords <= coordsTwo)  # Output: True
print(coords >= coordsTwo)  # Output: False