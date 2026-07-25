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

# My Contribution: Function to compute power (a raised to b)
def pow_number(a, b):
    # Initialize answer
    ans = 1

    # Check for invalid input
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        print("Please enter valid numbers!")
        return None

    # Handle negative exponent
    if b < 0:
        print("Negative exponents are not supported in this simple calculator.")
        return None

    # Handle exponent zero
    elif b == 0:
        print("Any number raised to the power 0 is 1")
        ans = 1

    # Compute power using a loop
    else:
        for i in range(1, int(b) + 1):
            ans = ans * a

    # Print result
    print("The value of", a, "raised to the power", b, "is", ans)
    return ans
