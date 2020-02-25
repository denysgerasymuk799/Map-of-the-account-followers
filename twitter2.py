import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl
import os


def create_account_users_json(acct):
    """

    :param acct: an account tha you inputed
    :return: a json file with all information about your account
    """
    # https://apps.twitter.com/
    # Create App and get the four strings, put them in hidden.py

    TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    if len(acct) < 1:
        return 'Enter an account that really exists'

    else:
        url = twurl.augment(TWITTER_URL,
                            {'screen_name': acct,
                             'count': '100'})
        connection = urllib.request.urlopen(url, context=ctx)
        data = connection.read().decode()

        js = json.loads(data)
        return_string = json.dumps(js, ensure_ascii=False, indent=4)

        headers = dict(connection.getheaders())

        # save to file to prevent HTTP Error 429: Too Many Requests for one account(lab 3.2)
        with open(os.path.join(os.getcwd(), 'jsons_dir', acct + "_data" + ".json"), "w", encoding="utf-8") as f:
            json.dump(js, f, ensure_ascii=False, indent=4)

        return return_string


if __name__ == '__main__':
    account = input('Enter Twitter Account:')
    print(create_account_users_json(account))
