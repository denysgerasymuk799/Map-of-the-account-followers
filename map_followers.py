import folium

from location_from_text import find_location_from_name


def followers_location_layer(layer_account):
    """

    :param layer_account: an account that you wrote
    :return: an object of markers that show locations and screen_names of follower
    """
    try:
        all_follower_locations = folium.FeatureGroup(name="Account followers' locations")

        followers_locations = find_location_from_name(layer_account)
        for follower in followers_locations:
            all_follower_locations.add_child(folium.Marker(location=[follower[1]["lat"], follower[1]["lng"]],
                                                           popup=follower[0],
                                                           icon=folium.Icon()))

        return all_follower_locations

    except TypeError:
        print("Something went wrong. Try to input other account")


def create_followers_map(account_map):
    """

    :param account_map: an account that you wrote
    Save a map in Account follower' locations.html
    """
    try:
        map = folium.Map(zoom_start=10, tiles="Stamen Terrain")
        map_all_follower_locations = followers_location_layer(account_map)
        map.add_child(map_all_follower_locations)
        map.add_child(folium.LayerControl())
        # map.save(outfile=os.path.join(os.getcwd(), 'templates', 'Account follower\' locations.html'))
        print("Finished. Please have look at the map Account follower\' locations.html")
        print("If you want to input other account, please, return to previous page")
        mapp = map.get_root().render()
        return mapp

    except TypeError:
        print("Something went wrong. Try to input other account")


if __name__ == "__main__":
    account = input('Enter Twitter Account:')
    create_followers_map(account)
