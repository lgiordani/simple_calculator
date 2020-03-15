from unittest import mock

from simple_calculator.meteorites import MeteoriteStats


def test_average_mass():
    metstats = MeteoriteStats()

    metstats.get_data = mock.Mock()
    metstats.get_data.return_value = [
        {
            "fall": "Fell",
            "geolocation": {
                "type": "Point",
                "coordinates": [6.08333, 50.775]
            },
            "id":"1",
            "mass":"21",
            "name":"Aachen",
            "nametype":"Valid",
            "recclass":"L5",
            "reclat":"50.775000",
            "reclong":"6.083330",
            "year":"1880-01-01T00:00:00.000"},
        {
            "fall": "Fell",
            "geolocation": {
                "type": "Point",
                "coordinates": [10.23333, 56.18333]
            },
            "id":"2",
            "mass":"720",
            "name":"Aarhus",
            "nametype":"Valid",
            "recclass":"H6",
            "reclat":"56.183330",
            "reclong":"10.233330",
            "year":"1951-01-01T00:00:00.000"
        }
    ]

    result = metstats.average_mass(metstats.get_data())

    assert result == 370.5
