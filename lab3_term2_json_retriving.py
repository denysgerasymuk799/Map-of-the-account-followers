import json
import os

from twitter2 import create_account_users_json


def print_dict_keys(key_json):
    """
    dict - > str
    key_json: a dictionary that you want to retrieve
    return: a key of dict that you chose
    """
    json_keys = []
    print()
    print("A list of dict keys")
    for num, key in enumerate(key_json.keys()):
        print(str(num + 1) + " " + key)
        json_keys.append(key)

    taking_key = input("Choose a number of key you want to get: ")
    taking_key = json_keys[int(taking_key) - 1]
    return taking_key


def print_list(list_key_json):
    """
    list - > str or list
    list_key_json: a list that you want to retrieve
    return: an element of list that you chose
    """
    print()
    print("The key is a list. The length of the list is ", len(list_key_json))
    print("Your value of chosen list key  is", list_key_json)
    num_list = input("Choose a number of element that you want to retrieve from 1 - {}\n".format(len(list_key_json)))
    list_key_json = list_key_json[int(num_list) - 1]
    return list_key_json


def json_retrieving(account_retrieve):
    """

    account_retrieve: an account, which api json you want to retrieve
    Print a values of dictionary that you choose from a list of dict or list elements
    """
    try:
        dir_name = os.path.join(os.getcwd(), 'jsons_dir')
        if account_retrieve + "_data" + ".json" not in os.listdir(dir_name):
            create_account_users_json(account)

        with open(os.path.join(dir_name, account_retrieve + "_data" + ".json"), "r", encoding='utf-8') as f:
            key_json = json.load(f)

        try:
            while isinstance(key_json, dict) or isinstance(key_json, list):
                if isinstance(key_json, dict):
                    taking_key = print_dict_keys(key_json)
                    key_json = key_json[taking_key]

                elif isinstance(key_json, list):
                    key_json = print_list(key_json)

                if not key_json:
                    break

        except ValueError:
            print("This number is not a number of dict or list that I can show.\n"
                  " Please, special numbers, in other case programe will stop.\n"
                  " Try ones more")
            while isinstance(key_json, dict) or isinstance(key_json, list):
                if isinstance(key_json, dict):
                    taking_key = print_dict_keys(key_json)
                    key_json = key_json[taking_key]

                elif isinstance(key_json, list):
                    key_json = print_list(key_json)

                if not key_json:
                    break

        print("Your value is ", key_json)

    except ValueError:
        print("Something went wrong. Try ones more")


if __name__ == '__main__':
    try:
        account = input('Enter Twitter Account: ')
        json_retrieving(account)

    except ValueError:
        print("Input existing account")
