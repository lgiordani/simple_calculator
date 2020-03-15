import urllib.request
import json

from simple_calculator.main import SimpleCalculator

URL = ("https://data.nasa.gov/resource/y77d-th95.json")


class MeteoriteStats:
    def get_data(self):
        with urllib.request.urlopen(URL) as url:
            return json.loads(url.read().decode())

    def average_mass(self, data):
        calculator = SimpleCalculator()

        masses = [float(d['mass']) for d in data if 'mass' in d]

        return calculator.avg(masses)
