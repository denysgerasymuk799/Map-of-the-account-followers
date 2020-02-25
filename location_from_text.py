import os
from geopy.geocoders import Nominatim

from twitter2 import create_account_users_json


def find_location_from_name(location_account):
    """
    str -> list
    :param location_account: an inputed account
    :return: a list of lists with follower screen_name, latitude and longitude
    """
    try:
        dir_name = os.getcwd()
        if location_account + "_data" + ".json" not in os.listdir(dir_name):
            create_account_users_json(location_account)

        location_account_json = create_account_users_json(location_account)

        geolocator = Nominatim(user_agent="specify_your_app_name_here", timeout=5)
        all_followers_location = []
        from geopy.extra.rate_limiter import RateLimiter
        geocode = RateLimiter(geolocator.geocode, min_delay_seconds=10, error_wait_seconds=15)
        for follower in location_account_json["users"]:
            try:
                location = geolocator.geocode(follower["location"])
                all_followers_location.append([follower["screen_name"],
                                               {"lat": location.latitude,
                                                "lng": location.longitude}])
            except:
                all_followers_location.append([follower["screen_name"], {"lat": 0, "lng": 0}])

        return all_followers_location

    except TypeError:
        print("Something went wrong. Try to input other account")
